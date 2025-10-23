# -*- coding: utf-8 -*-
"""
A股股票代码和名称获取脚本
调用akshare包的stock_info_a_code_name方法获取沪深京A股完整列表
支持JSON格式输出
"""

import akshare as ak
import pandas as pd
import json
from typing import Dict, Any


def stock_info_a_code_name() -> pd.DataFrame:
    """
    获取沪深京A股完整列表

    Returns:
        pd.DataFrame: 包含所有A股的代码和名称，列包括：
                    - code: 股票代码
                    - name: 股票名称
                    - market: 所属市场（sh/sz/bj）
    """
    try:
        # 直接调用akshare的stock_info_a_code_name方法
        df = ak.stock_info_a_code_name()

        # 确保返回数据包含必要的列
        if df.empty:
            print("警告：获取到的数据为空")
            return pd.DataFrame(columns=['code', 'name', 'market'])

        # 标准化列名（根据akshare实际返回的列名进行调整）
        if '代码' in df.columns and '名称' in df.columns:
            df = df.rename(columns={'代码': 'code', '名称': 'name'})
        elif 'code' not in df.columns:
            # 如果列名不匹配，尝试找到可能的列
            possible_code_cols = [col for col in df.columns if '码' in col or 'code' in col.lower()]
            possible_name_cols = [col for col in df.columns if '名' in col or 'name' in col.lower()]

            if possible_code_cols and possible_name_cols:
                df = df.rename(columns={
                    possible_code_cols[0]: 'code',
                    possible_name_cols[0]: 'name'
                })

        # 添加market列（如果不存在）
        if 'market' not in df.columns:
            df['market'] = df['code'].apply(_determine_market)

        # 确保返回的列顺序正确
        required_cols = ['code', 'name', 'market']
        available_cols = [col for col in required_cols if col in df.columns]

        return df[available_cols]

    except Exception as e:
        print(f"调用akshare.stock_info_a_code_name时发生错误: {e}")
        return pd.DataFrame(columns=['code', 'name', 'market'])


def _determine_market(code: str) -> str:
    """
    根据股票代码判断所属市场

    Args:
        code (str): 股票代码

    Returns:
        str: 市场代码（sh/sz/bj）
    """
    if pd.isna(code):
        return 'unknown'

    code_str = str(code).zfill(6)

    # 上交所代码规则
    if code_str.startswith(('6', '9')):
        return 'sh'
    # 深交所代码规则
    elif code_str.startswith(('0', '2', '3')):
        return 'sz'
    # 北交所代码规则
    elif code_str.startswith(('8', '4')):
        return 'bj'
    else:
        return 'unknown'


def stock_info_a_code_name_json() -> Dict[str, Dict[str, str]]:
    """
    获取沪深京A股完整列表并转换为JSON格式
    返回格式：{股票代码: {"code": 股票代码, "name": 股票名称, "market": 市场}}

    Returns:
        Dict[str, Dict[str, str]]: 股票信息的字典格式
    """
    try:
        df = stock_info_a_code_name()

        if df.empty:
            print("警告：获取到的数据为空")
            return {}

        # 转换为JSON格式
        result = {}
        for _, row in df.iterrows():
            code = str(row['code']).zfill(6)
            result[code] = {
                "code": code,
                "name": str(row['name']),
                "market": str(row['market'])
            }

        return result

    except Exception as e:
        print(f"转换JSON格式时发生错误: {e}")
        return {}


def save_stock_info_to_json(file_path: str = "stock_info.json") -> bool:
    """
    将A股信息保存到JSON文件

    Args:
        file_path (str): JSON文件保存路径

    Returns:
        bool: 保存是否成功
    """
    try:
        stock_data = stock_info_a_code_name_json()

        if not stock_data:
            print("没有数据可保存")
            return False

        # 确保文件扩展名为.json
        if not file_path.endswith('.json'):
            file_path += '.json'

        # 保存到文件，使用utf-8编码和中文格式化
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(stock_data, f, ensure_ascii=False, indent=2)

        print(f"成功保存 {len(stock_data)} 只股票信息到 {file_path}")
        return True

    except Exception as e:
        print(f"保存JSON文件时发生错误: {e}")
        return False


def load_stock_info_from_json(file_path: str) -> Dict[str, Dict[str, str]]:
    """
    从JSON文件加载股票信息

    Args:
        file_path (str): JSON文件路径

    Returns:
        Dict[str, Dict[str, str]]: 股票信息的字典格式
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            stock_data = json.load(f)

        print(f"成功从 {file_path} 加载 {len(stock_data)} 只股票信息")
        return stock_data

    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
        return {}
    except Exception as e:
        print(f"加载JSON文件时发生错误: {e}")
        return {}


def stock_info_sh_name_code(symbol: str = "主板A股") -> pd.DataFrame:
    """
    获取上海证券交易所股票列表

    Args:
        symbol (str): 可选 "主板A股", "主板B股", "科创板"

    Returns:
        pd.DataFrame: 上交所股票列表信息
    """
    try:
        return ak.stock_info_sh_name_code(symbol=symbol)
    except Exception as e:
        print(f"调用akshare.stock_info_sh_name_code时发生错误: {e}")
        return pd.DataFrame()


def stock_info_sz_name_code(symbol: str = "A股列表") -> pd.DataFrame:
    """
    获取深圳证券交易所股票列表

    Args:
        symbol (str): 可选 "A股列表", "B股列表", "CDR列表", "AB股列表"

    Returns:
        pd.DataFrame: 深交所股票列表信息
    """
    try:
        return ak.stock_info_sz_name_code(symbol=symbol)
    except Exception as e:
        print(f"调用akshare.stock_info_sz_name_code时发生错误: {e}")
        return pd.DataFrame()


def stock_info_bj_name_code() -> pd.DataFrame:
    """
    获取北京证券交易所股票列表

    Returns:
        pd.DataFrame: 北交所股票列表信息
    """
    try:
        return ak.stock_info_bj_name_code()
    except Exception as e:
        print(f"调用akshare.stock_info_bj_name_code时发生错误: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    # 测试代码
    print("正在调用akshare获取A股完整列表...")
    a_stock_list = stock_info_a_code_name()

    if not a_stock_list.empty:
        print(f"成功获取 {len(a_stock_list)} 只A股股票")
        print(f"数据列: {list(a_stock_list.columns)}")
        print("\n前10只股票:")
        print(a_stock_list.head(10))

        if 'market' in a_stock_list.columns:
            print(f"\n按市场分布:")
            market_count = a_stock_list['market'].value_counts()
            print(market_count)

        # 演示JSON格式转换
        print("\n" + "="*50)
        print("演示JSON格式转换:")
        stock_json = stock_info_a_code_name_json()

        # 显示前5只股票的JSON格式
        sample_stocks = list(stock_json.items())[:5]
        for code, info in sample_stocks:
            print(f'  "{code}": {{')
            print(f'    "code": "{info["code"]}",')
            print(f'    "name": "{info["name"]}",')
            print(f'    "market": "{info["market"]}"')
            print(f'  }},')

        print(f"\nJSON格式总数据量: {len(stock_json)} 只股票")

        # 保存到JSON文件
        print("\n" + "="*50)
        print("保存JSON文件...")
        if save_stock_info_to_json("stock_base_info.json"):
            print("JSON文件保存成功！")
        else:
            print("JSON文件保存失败！")

    else:
        print("获取A股列表失败")