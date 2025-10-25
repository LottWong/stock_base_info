#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A股股票基础信息批量获取脚本
从stock_code_name.py获取所有股票代码，从stock_base_handle.py获取基础信息
最终将所有股票信息保存到JSON文件
"""

import sys
import os
import json
import random
from datetime import datetime
from typing import Dict, Any, List
import time
import traceback

# 添加当前目录到Python路径，以便导入本地模块
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from stock_code_name import stock_info_a_code_name_json
from stock_base_handle import get_stock_info


class SmartDelayController:
    """智能延迟控制器"""

    def __init__(self, base_delay: float = 1.0, max_delay: float = 5.0):
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.current_delay = base_delay
        self.consecutive_errors = 0
        self.request_times = []

    def get_delay(self) -> float:
        """获取当前应该使用的延迟时间"""
        # 添加随机变化，避免固定模式
        random_factor = random.uniform(0.7, 1.3)
        delay = min(self.current_delay * random_factor, self.max_delay)

        # 如果最近请求过于频繁，适当增加延迟
        if len(self.request_times) >= 3:
            recent_requests = self.request_times[-3:]
            if recent_requests[-1] - recent_requests[0] < 2:  # 3次请求在2秒内
                delay *= 1.5

        return max(delay, 0.1)  # 最小延迟0.1秒

    def record_success(self):
        """记录成功请求"""
        self.consecutive_errors = 0
        self.current_delay = max(self.current_delay * 0.95, self.base_delay)  # 逐渐恢复
        self.request_times.append(time.time())
        # 只保留最近的请求记录
        self.request_times = self.request_times[-10:]

    def record_error(self):
        """记录错误请求"""
        self.consecutive_errors += 1
        # 连续错误时增加延迟
        if self.consecutive_errors >= 2:
            self.current_delay = min(self.current_delay * 1.5, self.max_delay)


class SafeRequestHandler:
    """安全的请求处理器"""

    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries

    def safe_request(self, stock_code: str, delay_controller: SmartDelayController) -> Dict[str, Any]:
        """安全地获取股票信息"""
        last_error = None

        for attempt in range(self.max_retries):
            try:
                print(f"  尝试获取 {stock_code} (第{attempt + 1}次)")

                # 执行请求
                stock_info = get_stock_info(stock_code)

                if stock_info:
                    delay_controller.record_success()
                    return stock_info
                else:
                    # API返回空数据
                    delay_controller.record_error()
                    last_error = "API返回空数据"

            except Exception as e:
                last_error = str(e)
                delay_controller.record_error()

                # 检查是否是网络相关错误
                if any(keyword in str(e).lower() for keyword in ['timeout', 'connection', 'network']):
                    print(f"  网络错误，等待重试: {e}")
                    time.sleep(2 * (attempt + 1))  # 网络错误时增加等待时间
                else:
                    print(f"  请求失败，等待重试: {e}")

            # 如果不是最后一次尝试，则等待后重试
            if attempt < self.max_retries - 1:
                wait_time = delay_controller.get_delay()
                print(f"  等待 {wait_time:.1f} 秒后重试...")
                time.sleep(wait_time)

        # 所有重试都失败了
        error_info = {
            'status': 'failed',
            'error': last_error or '未知错误',
            'attempts': self.max_retries
        }
        return error_info


class CheckpointManager:
    """断点续传管理器"""

    def __init__(self, checkpoint_file: str = "stock_progress_checkpoint.json"):
        self.checkpoint_file = checkpoint_file
        self.processed_codes = set()
        self.failed_codes = set()
        self.total_processed = 0

    def load_checkpoint(self) -> bool:
        """加载断点文件"""
        try:
            if os.path.exists(self.checkpoint_file):
                with open(self.checkpoint_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.processed_codes = set(data.get('processed_codes', []))
                    self.failed_codes = set(data.get('failed_codes', []))
                    self.total_processed = data.get('total_processed', 0)
                    print(f"✓ 加载断点文件: {len(self.processed_codes)} 已处理, {len(self.failed_codes)} 已失败")
                    return True
            else:
                print("✓ 未找到断点文件，从头开始处理")
                return False
        except Exception as e:
            print(f"✗ 加载断点文件失败: {e}")
            return False

    def save_checkpoint(self):
        """保存断点文件"""
        try:
            data = {
                'processed_codes': list(self.processed_codes),
                'failed_codes': list(self.failed_codes),
                'total_processed': self.total_processed,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            with open(self.checkpoint_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"✗ 保存断点文件失败: {e}")
            return False

    def is_processed(self, code: str) -> bool:
        """检查股票代码是否已处理"""
        return code in self.processed_codes

    def is_failed(self, code: str) -> bool:
        """检查股票代码是否已标记为失败"""
        return code in self.failed_codes

    def mark_processed(self, code: str):
        """标记股票代码为已处理"""
        self.processed_codes.add(code)
        self.total_processed += 1

    def mark_failed(self, code: str):
        """标记股票代码为失败"""
        self.failed_codes.add(code)

    def get_remaining_count(self, total_codes: set) -> int:
        """获取剩余未处理的股票数量"""
        return len(total_codes - self.processed_codes)

    def get_summary(self) -> str:
        """获取处理摘要"""
        return (f"已处理: {len(self.processed_codes)}, "
                f"失败: {len(self.failed_codes)}, "
                f"总计: {self.total_processed}")


def get_all_stocks_base_info(batch_size: int = 10, delay: float = 2.0,
                           test_mode: bool = False, checkpoint_file: str = None) -> Dict[str, Dict[str, Any]]:
    """
    获取所有A股股票的基础信息

    参数:
        batch_size (int): 每批处理的股票数量，用于控制进度显示
        delay (float): 每只股票之间的延迟时间（秒），避免请求过于频繁
        test_mode (bool): 是否为测试模式，只获取前10+后10只股票

    返回:
        Dict[str, Dict[str, Any]]: 所有股票的基础信息，格式为 {股票代码: 股票信息字典}
    """
    print("=" * 80)
    if test_mode:
        print("开始批量获取A股基础信息 [测试模式 - 仅前10+后10只股票]")
    else:
        print("开始批量获取A股基础信息")
    print(f"处理批次大小: {batch_size}")
    print(f"请求延迟: {delay}秒")
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # 1. 获取所有股票代码
    print("步骤1: 获取所有A股股票代码列表...")
    stock_codes = stock_info_a_code_name_json()

    if not stock_codes:
        print("错误: 无法获取股票代码列表")
        return {}

    total_stocks = len(stock_codes)
    print(f"✓ 成功获取 {total_stocks} 只股票代码")

    # 如果是测试模式，只取前10+后10只股票
    if test_mode:
        all_codes = list(stock_codes.items())
        test_codes = all_codes[:10] + all_codes[-10:]  # 前10+后10
        stock_codes = dict(test_codes)
        print(f"✓ 测试模式：已筛选为 {len(stock_codes)} 只股票（前10只+后10只）")

    # 2. 初始化断点续传管理器
    checkpoint_file = checkpoint_file or ("test_stock_progress_checkpoint.json" if test_mode else "stock_progress_checkpoint.json")
    checkpoint_manager = CheckpointManager(checkpoint_file)

    print(f"\n步骤2: 初始化断点续传...")
    has_checkpoint = checkpoint_manager.load_checkpoint()

    # 3. 初始化安全请求处理器和智能延迟控制器
    print(f"\n步骤3: 初始化安全请求处理器...")
    delay_controller = SmartDelayController(base_delay=delay, max_delay=10.0)
    request_handler = SafeRequestHandler(max_retries=3)

    print(f"  基础延迟: {delay}秒")
    print(f"  最大延迟: 10.0秒")
    print(f"  最大重试次数: 3次")
    print(f"  断点文件: {checkpoint_file}")

    # 4. 筛选待处理的股票（排除已处理的）
    total_codes = set(stock_codes.keys())
    if has_checkpoint:
        remaining_codes = total_codes - checkpoint_manager.processed_codes
        print(f"  断点状态: {checkpoint_manager.get_summary()}")
        print(f"  剩余待处理: {len(remaining_codes)} 只股票")

        # 如果有已经失败且需要重试的代码，可以选择是否包含它们
        # 这里我们跳过已经处理过的，包括失败的
        filtered_stock_codes = {code: stock_codes[code] for code in remaining_codes}
    else:
        filtered_stock_codes = stock_codes

    if not filtered_stock_codes:
        print("✓ 所有股票已处理完成")
        return {}

    # 加载已存在的数据
    existing_data = {}
    if has_checkpoint:
        existing_data_file = "existing_data_temp.json"
        if os.path.exists(existing_data_file):
            existing_data = load_stock_base_info_from_json(existing_data_file)

    actual_total = len(filtered_stock_codes)
    print(f"\n步骤4: 开始处理剩余 {actual_total} 只股票...")
    all_stock_info = existing_data
    success_count = 0
    fail_count = 0
    batch_processed = 0

    try:
        for i, (code, basic_info) in enumerate(filtered_stock_codes.items(), 1):
            print(f"\n处理进度: {i}/{actual_total} ({i/actual_total*100:.1f}%) [总计: {len(checkpoint_manager.processed_codes)+i}]")
            print(f"正在处理: {code} - {basic_info.get('name', '未知')} ({basic_info.get('market', 'unknown')})")

            # 跳过已处理的股票（双重保险）
            if checkpoint_manager.is_processed(code):
                print(f"⏭️  跳过已处理的股票: {code}")
                continue

            # 使用安全请求处理器获取数据
            stock_info_result = request_handler.safe_request(code, delay_controller)

            # 合并基本信息
            base_info = {
                'code': code,
                'name': basic_info.get('name', ''),
                'market': basic_info.get('market', ''),
                'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }

            if 'status' not in stock_info_result:  # 成功获取
                combined_info = {**base_info, **stock_info_result}
                all_stock_info[code] = combined_info
                checkpoint_manager.mark_processed(code)
                success_count += 1
                batch_processed += 1
                print(f"✓ 成功获取 {code} 的信息，共 {len(stock_info_result)} 个字段")
            else:  # 获取失败
                error_info = {**base_info, **stock_info_result}
                all_stock_info[code] = error_info
                checkpoint_manager.mark_failed(code)
                fail_count += 1
                batch_processed += 1
                print(f"✗ 获取 {code} 信息失败: {stock_info_result.get('error', '未知错误')}")

            # 每处理一定数量后保存断点
            if batch_processed >= batch_size:
                if checkpoint_manager.save_checkpoint():
                    print(f"💾 已保存断点: {checkpoint_manager.get_summary()}")
                    batch_processed = 0

            # 显示批次统计
            if i % batch_size == 0:
                batch_time = datetime.now().strftime('%H:%M:%S')
                current_delay = delay_controller.get_delay()
                print(f"\n批次统计 ({i}/{actual_total}):")
                print(f"  成功: {success_count}, 失败: {fail_count}")
                print(f"  当前时间: {batch_time}")
                print(f"  当前延迟: {current_delay:.2f}秒")
                print(f"  剩余: {checkpoint_manager.get_remaining_count(total_codes)} 只")

            # 智能延迟控制
            if i < actual_total:  # 最后一只股票不需要延迟
                wait_time = delay_controller.get_delay()
                print(f"  等待 {wait_time:.1f} 秒...")
                time.sleep(wait_time)

    except KeyboardInterrupt:
        print(f"\n\n⏹️ 用户中断了程序执行")
        print(f"💾 正在保存断点...")
        checkpoint_manager.save_checkpoint()
        print(f"✓ 断点已保存，下次可以从这里继续")
        print(f"  当前进度: {checkpoint_manager.get_summary()}")
        print(f"  剩余股票: {checkpoint_manager.get_remaining_count(total_codes)} 只")
        return all_stock_info

    # 最终保存断点
    checkpoint_manager.save_checkpoint()

    # 合并已处理的数据
    final_processed = len(checkpoint_manager.processed_codes)
    final_success = len([s for s in all_stock_info.values() if s.get('status') not in ['failed', 'error']])
    final_failed = final_processed - final_success

    print(f"\n" + "=" * 80)
    print("批量获取完成!")
    print(f"总计: {total_stocks} 只股票")
    print(f"成功: {success_count} 只")
    print(f"失败: {fail_count} 只")
    print(f"成功率: {success_count/total_stocks*100:.1f}%")
    print(f"结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    return all_stock_info


def save_stock_base_info_to_json(stock_data: Dict[str, Dict[str, Any]],
                                file_path: str = "stock_base_info.json") -> bool:
    """
    将股票基础信息保存到JSON文件

    参数:
        stock_data (Dict): 股票基础信息字典
        file_path (str): 保存路径

    返回:
        bool: 保存是否成功
    """
    try:
        if not stock_data:
            print("错误: 没有数据可保存")
            return False

        # 确保文件扩展名为.json
        if not file_path.endswith('.json'):
            file_path += '.json'

        # 创建保存目录（如果不存在）
        save_dir = os.path.dirname(file_path)
        if save_dir and not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

        # 保存到文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(stock_data, f, ensure_ascii=False, indent=2)

        file_size = os.path.getsize(file_path) / (1024 * 1024)  # MB
        print(f"✓ 成功保存 {len(stock_data)} 只股票信息到 {file_path}")
        print(f"  文件大小: {file_size:.2f} MB")

        return True

    except Exception as e:
        print(f"✗ 保存文件时发生错误: {e}")
        return False


def load_stock_base_info_from_json(file_path: str) -> Dict[str, Dict[str, Any]]:
    """
    从JSON文件加载股票基础信息

    参数:
        file_path (str): JSON文件路径

    返回:
        Dict[str, Dict[str, Any]]: 股票基础信息字典
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            stock_data = json.load(f)

        print(f"✓ 成功从 {file_path} 加载 {len(stock_data)} 只股票信息")
        return stock_data

    except FileNotFoundError:
        print(f"✗ 文件 {file_path} 不存在")
        return {}
    except Exception as e:
        print(f"✗ 加载文件时发生错误: {e}")
        return {}


def clear_checkpoint(checkpoint_file: str = "stock_progress_checkpoint.json"):
    """
    清理断点文件

    参数:
        checkpoint_file (str): 断点文件路径
    """
    try:
        if os.path.exists(checkpoint_file):
            os.remove(checkpoint_file)
            print(f"✓ 已删除断点文件: {checkpoint_file}")
        else:
            print(f"✓ 断点文件不存在: {checkpoint_file}")

        # 同时删除临时数据文件
        temp_file = "existing_data_temp.json"
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"✓ 已删除临时数据文件: {temp_file}")

    except Exception as e:
        print(f"✗ 删除断点文件时出错: {e}")


def generate_summary_report(stock_data: Dict[str, Dict[str, Any]]) -> None:
    """
    生成数据摘要报告

    参数:
        stock_data: 股票基础信息数据
    """
    if not stock_data:
        print("没有数据可分析")
        return

    print("\n" + "=" * 80)
    print("数据摘要报告")
    print("=" * 80)

    total_stocks = len(stock_data)
    success_stocks = len([s for s in stock_data.values() if s.get('status') != 'failed' and s.get('status') != 'error'])
    failed_stocks = total_stocks - success_stocks

    print(f"总股票数量: {total_stocks}")
    print(f"成功获取: {success_stocks} ({success_stocks/total_stocks*100:.1f}%)")
    print(f"获取失败: {failed_stocks} ({failed_stocks/total_stocks*100:.1f}%)")

    # 市场分布
    market_count = {}
    for stock in stock_data.values():
        market = stock.get('market', 'unknown')
        market_count[market] = market_count.get(market, 0) + 1

    print(f"\n市场分布:")
    for market, count in sorted(market_count.items()):
        print(f"  {market}: {count} 只股票")

    # 字段统计
    if success_stocks > 0:
        success_stock = next(s for s in stock_data.values() if s.get('status') != 'failed' and s.get('status') != 'error')
        field_count = len(success_stock) - 4  # 减去 code, name, market, update_time
        print(f"\n平均字段数量: {field_count}")
        print(f"主要字段示例: {list(success_stock.keys())[:10]}")

    print("=" * 80)


def test_stock_info():
    """
    测试函数 - 仅获取前10+后10只股票信息
    """
    print("测试股票基础信息获取功能")
    print("=" * 80)

    # 测试模式配置
    test_output_file = "test_stock_base_info.json"
    batch_size = 5   # 每5只股票显示一次进度
    delay = 0.5      # 测试时缩短请求间隔

    try:
        # 获取测试股票基础信息（前10+后10只）
        stock_data = get_all_stocks_base_info(batch_size=batch_size, delay=delay, test_mode=True)

        if stock_data:
            # 保存到测试JSON文件
            print(f"\n正在保存测试数据到 {test_output_file}...")
            if save_stock_base_info_to_json(stock_data, test_output_file):
                # 生成测试摘要报告
                generate_summary_report(stock_data)

                print(f"\n测试完成！测试股票基础信息已保存到 {test_output_file}")

                # 显示测试的股票代码列表
                print(f"\n测试股票代码列表:")
                for code, info in stock_data.items():
                    status = "成功" if info.get('status') not in ['failed', 'error'] else "失败"
                    print(f"  {code} - {info.get('name', '未知')} [{status}]")

            else:
                print("\n测试保存文件失败")
        else:
            print("\n测试没有获取到任何股票信息")

    except KeyboardInterrupt:
        print(f"\n\n用户中断了测试")
    except Exception as e:
        print(f"\n测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()


def main():
    """
    主函数 - 执行完整的股票信息获取和保存流程
    """
    print("A股股票基础信息批量获取脚本")
    print("=" * 80)

    # 配置参数 - 生产环境使用更保守的设置
    output_file = "stock_base_info.json"
    batch_size = 10  # 每10只股票显示一次进度
    delay = 2.0     # 增加请求间隔到2秒，降低封禁风险

    try:
        # 获取所有股票基础信息
        stock_data = get_all_stocks_base_info(batch_size=batch_size, delay=delay)

        if stock_data:
            # 保存到JSON文件
            print(f"\n正在保存数据到 {output_file}...")
            if save_stock_base_info_to_json(stock_data, output_file):
                # 生成摘要报告
                generate_summary_report(stock_data)

                print(f"\n任务完成！股票基础信息已保存到 {output_file}")
            else:
                print("\n保存文件失败")
        else:
            print("\n没有获取到任何股票信息")

    except KeyboardInterrupt:
        print(f"\n\n用户中断了程序执行")
    except Exception as e:
        print(f"\n程序执行过程中发生错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    import sys

    # 检查命令行参数
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "test":
            # 运行测试模式
            test_stock_info()
        elif command == "clear":
            # 清理断点文件
            checkpoint_file = sys.argv[2] if len(sys.argv) > 2 else "stock_progress_checkpoint.json"
            clear_checkpoint(checkpoint_file)
            print("断点文件已清理，下次运行将从头开始")
        elif command == "help":
            # 显示帮助信息
            print("A股股票基础信息批量获取脚本")
            print("=" * 50)
            print("使用方法:")
            print("  python stock_base_multi_handle.py           # 完整模式（获取所有股票）")
            print("  python stock_base_multi_handle.py test       # 测试模式（前10+后10只股票）")
            print("  python stock_base_multi_handle.py clear      # 清理断点文件")
            print("  python stock_base_multi_handle.py clear [文件名] # 清理指定断点文件")
            print("  python stock_base_multi_handle.py help       # 显示帮助信息")
            print("")
            print("断点续传:")
            print("  - 程序会自动保存进度到 stock_progress_checkpoint.json")
            print("  - 如果中断，下次运行会自动从断点继续")
            print("  - 使用 'clear' 命令可以重置进度")
            print("")
            print("安全特性:")
            print("  - 智能延迟控制，避免API封禁")
            print("  - 自动重试机制（最多3次）")
            print("  - 断点续传，支持中断后继续")
            print("  - 错误处理和状态记录")
        else:
            print(f"未知命令: {command}")
            print("使用 'python stock_base_multi_handle.py help' 查看帮助信息")
    else:
        # 运行完整模式
        main()