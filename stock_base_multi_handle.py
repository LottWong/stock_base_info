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
from datetime import datetime
from typing import Dict, Any, List
import time

# 添加当前目录到Python路径，以便导入本地模块
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from stock_code_name import stock_info_a_code_name_json
from stock_base_handle import get_stock_info


def get_all_stocks_base_info(batch_size: int = 10, delay: float = 1.0, test_mode: bool = False) -> Dict[str, Dict[str, Any]]:
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

    # 2. 批量获取每只股票的基础信息
    print(f"\n步骤2: 开始批量获取股票基础信息...")
    all_stock_info = {}
    success_count = 0
    fail_count = 0

    for i, (code, basic_info) in enumerate(stock_codes.items(), 1):
        print(f"\n处理进度: {i}/{total_stocks} ({i/total_stocks*100:.1f}%)")
        print(f"正在处理: {code} - {basic_info.get('name', '未知')} ({basic_info.get('market', 'unknown')})")

        try:
            # 获取股票基础信息
            stock_info = get_stock_info(code)

            if stock_info:
                # 合并基本信息和详细信息
                combined_info = {
                    'code': code,
                    'name': basic_info.get('name', ''),
                    'market': basic_info.get('market', ''),
                    'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    **stock_info  # 展开所有从stock_base_handle.py获取的字段
                }

                all_stock_info[code] = combined_info
                success_count += 1
                print(f"✓ 成功获取 {code} 的信息，共 {len(stock_info)} 个字段")
            else:
                # 即使获取详细信息失败，也保存基本信息
                failed_info = {
                    'code': code,
                    'name': basic_info.get('name', ''),
                    'market': basic_info.get('market', ''),
                    'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'status': 'failed',
                    'error': '无法获取详细信息'
                }
                all_stock_info[code] = failed_info
                fail_count += 1
                print(f"✗ 获取 {code} 信息失败")

        except Exception as e:
            # 处理异常情况
            error_info = {
                'code': code,
                'name': basic_info.get('name', ''),
                'market': basic_info.get('market', ''),
                'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'status': 'error',
                'error': str(e)
            }
            all_stock_info[code] = error_info
            fail_count += 1
            print(f"✗ 处理 {code} 时发生错误: {e}")

        # 显示批次统计
        if i % batch_size == 0:
            batch_time = datetime.now().strftime('%H:%M:%S')
            print(f"\n批次统计 ({i}/{total_stocks}):")
            print(f"  成功: {success_count}, 失败: {fail_count}")
            print(f"  当前时间: {batch_time}")

        # 延迟控制
        if delay > 0 and i < total_stocks:  # 最后一只股票不需要延迟
            time.sleep(delay)

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

    # 配置参数
    output_file = "stock_base_info.json"
    batch_size = 10  # 每10只股票显示一次进度
    delay = 1.0     # 请求间隔1秒

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
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # 运行测试模式
        test_stock_info()
    else:
        # 运行完整模式
        main()