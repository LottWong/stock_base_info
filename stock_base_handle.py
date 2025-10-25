#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票基础信息统一获取接口
结合cninfo和xqinfo两个数据源，提供统一的股票信息获取功能
"""

import sys
import os
from datetime import datetime

# 添加当前目录到Python路径，以便导入本地模块
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from stock_base_cninfo import get_stock_basic_info as get_cninfo_info
# 导入xqinfo模块
from stock_base_xqinfo import get_xueqiu_stock_info

def get_stock_info(stock_code):
    """
    统一获取股票基础信息的接口

    参数:
        stock_code (str): 股票代码，如"600030"

    返回:
        dict: 包含从两个数据源获取的股票信息的扁平字典
              包含cninfo和xqinfo的所有字段，直接合并到一个字典中
    """

    print(f"开始获取股票 {stock_code} 的基础信息...")
    print(f"获取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    result = {}

    # 获取cninfo数据
    print("正在从巨潮资讯(cninfo)获取数据...")
    try:
        en_info, cn_info = get_cninfo_info(stock_code)
        if en_info:
            result.update(en_info)
            print("✓ cninfo数据获取成功")
        else:
            print("✗ cninfo数据获取失败")
    except Exception as e:
        print(f"✗ cninfo数据获取出错: {e}")

    # 获取xqinfo数据
    print("正在从雪球(xqinfo)获取数据...")
    try:
        xq_info = get_xqinfo_stock_info(stock_code)
        if xq_info:
            result.update(xq_info)
            print("✓ xqinfo数据获取成功")
        else:
            print("✗ xqinfo数据获取失败")
    except Exception as e:
        print(f"✗ xqinfo数据获取出错: {e}")

    print("-" * 60)

    return result

def get_xqinfo_stock_info(stock_code):
    """
    获取雪球股票信息的包装函数
    """
    try:
        return get_xueqiu_stock_info(stock_code)
    except ImportError as e:
        print(f"导入stock_base_xqinfo模块失败: {e}")
        return None


def print_summary(result):
    """
    打印获取结果摘要

    参数:
        result (dict): 统一的获取结果
    """
    print("\n" + "=" * 60)
    print("获取结果摘要")
    print("=" * 60)
    print(f"共获取到 {len(result)} 个字段")

    # cninfo字段
    cninfo_fields = [k for k in result.keys() if k.startswith('cninfo_')]
    if cninfo_fields:
        company_name = result.get('cninfo_name', '未知')
        a_share_code = result.get('cninfo_code', '未知')
        print(f"cninfo: ✓ 成功 - {company_name} ({a_share_code})")
        print(f"  包含 {len(cninfo_fields)} 个cninfo字段")
    else:
        print("cninfo: ✗ 失败")

    # xqinfo字段
    xqinfo_fields = [k for k in result.keys() if k.startswith('xqinfo_')]
    if xqinfo_fields:
        company_name = result.get('xqinfo_org_name_cn', '未知')
        print(f"xqinfo: ✓ 成功 - {company_name}")
        print(f"  包含 {len(xqinfo_fields)} 个xqinfo字段")
    else:
        print("xqinfo: ✗ 失败")

    print("=" * 60)

def main():
    """
    主函数 - 演示如何使用统一接口
    """
    print("股票基础信息统一获取接口演示")
    print("=" * 60)

    # 测试股票代码
    stock_code = "002709"  # 中信证券

    # 使用统一接口获取股票信息
    print(f"\n获取股票 {stock_code} 的基础信息:")
    result = get_stock_info(stock_code)
    # print_summary(result)
    print(result)

if __name__ == "__main__":
    main()