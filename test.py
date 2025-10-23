#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
akshare股票基础信息接口测试
根据md/基础信息获取方法.md文档中的接口进行测试
"""

import akshare as ak
import pandas as pd
from datetime import datetime

def test_stock_individual_info_em():
    """测试东方财富个股信息接口"""
    print("=" * 50)
    print("1. 测试 stock_individual_info_em - 东方财富个股信息")
    print("=" * 50)

    try:
        # 使用中信证券作为测试样例
        df = ak.stock_individual_info_em(symbol="600030")
        print(f"数据形状: {df.shape}")
        print("\n前5行数据:")
        print(df.head())
        print("\n列名:")
        print(df.columns.tolist())
        print("✓ 接口测试成功\n")
    except Exception as e:
        print(f"✗ 接口测试失败: {e}\n")

def test_stock_profile_cninfo():
    """测试巨潮资讯公司概况接口"""
    print("=" * 50)
    print("2. 测试 stock_profile_cninfo - 巨潮资讯公司概况")
    print("=" * 50)

    try:
        df = ak.stock_profile_cninfo(symbol="600030")
        print(f"数据形状: {df.shape}")
        print("\n数据内容:")
        print(df)
        print("\n列名:")
        print(df.columns.tolist())
        print("✓ 接口测试成功\n")
    except Exception as e:
        print(f"✗ 接口测试失败: {e}\n")

def test_stock_individual_basic_info_xq():
    """测试雪球公司概况接口"""
    print("=" * 50)
    print("3. 测试 stock_individual_basic_info_xq - 雪球公司概况")
    print("=" * 50)

    try:
        # 注意雪球需要带交易所前缀的股票代码
        df = ak.stock_individual_basic_info_xq(symbol="SH601127")
        print(f"数据形状: {df.shape}")
        print("\n数据内容:")
        print(df)
        print("\n列名:")
        print(df.columns.tolist())
        print("✓ 接口测试成功\n")
    except Exception as e:
        print(f"✗ 接口测试失败: {e}\n")

def test_stock_hold_control_cninfo():
    """测试巨潮资讯控制股东信息接口"""
    print("=" * 50)
    print("4. 测试 stock_hold_control_cninfo - 巨潮资讯控制股东信息")
    print("=" * 50)

    try:
        df = ak.stock_hold_control_cninfo(symbol="600030")
        print(f"数据形状: {df.shape}")
        print("\n数据内容:")
        print(df)
        print("\n列名:")
        print(df.columns.tolist())
        print("✓ 接口测试成功\n")
    except Exception as e:
        print(f"✗ 接口测试失败: {e}\n")

def test_stock_ipo_summary_cninfo():
    """测试巨潮资讯IPO信息接口"""
    print("=" * 50)
    print("5. 测试 stock_ipo_summary_cninfo - 巨潮资讯IPO信息")
    print("=" * 50)

    try:
        df = ak.stock_ipo_summary_cninfo(symbol="600030")
        print(f"数据形状: {df.shape}")
        print("\n数据内容:")
        print(df)
        print("\n列名:")
        print(df.columns.tolist())
        print("✓ 接口测试成功\n")
    except Exception as e:
        print(f"✗ 接口测试失败: {e}\n")

def test_stock_register_sh():
    """测试上交所注册股票列表接口"""
    print("=" * 50)
    print("6. 测试 stock_register_sh - 上交所注册股票列表")
    print("=" * 50)

    try:
        df = ak.stock_register_sh()
        print(f"数据形状: {df.shape}")
        print("\n前5行数据:")
        print(df.head())
        print("\n列名:")
        print(df.columns.tolist())
        print("✓ 接口测试成功\n")
    except Exception as e:
        print(f"✗ 接口测试失败: {e}\n")

def test_stock_register_sz():
    """测试深交所注册股票列表接口"""
    print("=" * 50)
    print("7. 测试 stock_register_sz - 深交所注册股票列表")
    print("=" * 50)

    try:
        df = ak.stock_register_sz()
        print(f"数据形状: {df.shape}")
        print("\n前5行数据:")
        print(df.head())
        print("\n列名:")
        print(df.columns.tolist())
        print("✓ 接口测试成功\n")
    except Exception as e:
        print(f"✗ 接口测试失败: {e}\n")

def test_stock_register_bj():
    """测试北交所注册股票列表接口"""
    print("=" * 50)
    print("8. 测试 stock_register_bj - 北交所注册股票列表")
    print("=" * 50)

    try:
        df = ak.stock_register_bj()
        print(f"数据形状: {df.shape}")
        print("\n前5行数据:")
        print(df.head())
        print("\n列名:")
        print(df.columns.tolist())
        print("✓ 接口测试成功\n")
    except Exception as e:
        print(f"✗ 接口测试失败: {e}\n")

def main():
    """主函数，执行所有测试"""
    print("开始测试akshare股票基础信息接口")
    print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("测试股票: 600030 (中信证券)")
    print()

    # 测试所有接口
    test_stock_individual_info_em()
    test_stock_profile_cninfo()
    test_stock_individual_basic_info_xq()
    test_stock_hold_control_cninfo()
    test_stock_ipo_summary_cninfo()
    test_stock_register_sh()
    test_stock_register_sz()
    test_stock_register_bj()

    print("=" * 50)
    print("所有接口测试完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()