#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
akshare股票基础信息接口测试
根据md/基础信息获取方法.md文档中的接口进行测试
"""

import akshare as ak
import pandas as pd
from datetime import datetime

# 设置pandas显示选项，显示完整内容
pd.set_option('display.max_columns', None)      # 显示所有列
pd.set_option('display.max_rows', None)         # 显示所有行
pd.set_option('display.width', None)           # 不限制列宽
pd.set_option('display.max_colwidth', None)     # 不限制列内容宽度
pd.set_option('display.expand_frame_repr', False)  # 不换行显示

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
        print("√ 接口测试成功\n")
    except Exception as e:
        print(f"× 接口测试失败: {e}\n")

def test_stock_profile_cninfo():
    """测试巨潮资讯公司概况接口"""
    print("=" * 50)
    print("2. 测试 stock_profile_cninfo - 巨潮资讯公司概况")
    print("=" * 50)

    try:
        df = ak.stock_profile_cninfo(symbol="600030")
        print(f"数据形状: {df.shape}")

        # 按照指定格式显示数据
        print("\n数据内容:")
        if not df.empty:
            for _, row in df.iterrows():
                print(f"公司名称:{row.get('公司名称', '')}")
                print(f"英文名称:{row.get('英文名称', '')}")
                print(f"曾用简称:{row.get('曾用简称', '')}")
                print(f"A股代码:{row.get('A股代码', '')}")
                print(f"A股简称:{row.get('A股简称', '')}")
                print(f"B股代码:{row.get('B股代码', '')}")
                print(f"B股简称:{row.get('B股简称', '')}")
                print(f"H股代码:{row.get('H股代码', '')}")
                print(f"H股简称:{row.get('H股简称', '')}")
                print(f"入选指数:{row.get('入选指数', '')}")
                print(f"所属市场:{row.get('所属市场', '')}")
                print(f"所属行业:{row.get('所属行业', '')}")
                print(f"法人代表:{row.get('法人代表', '')}")
                print(f"注册资金:{row.get('注册资金', '')}")
                print(f"成立日期:{row.get('成立日期', '')}")
                print(f"上市日期:{row.get('上市日期', '')}")
                print(f"官方网站:{row.get('官方网站', '')}")
                print(f"电子邮箱:{row.get('电子邮箱', '')}")
                print(f"联系电话:{row.get('联系电话', '')}")
                print(f"传真:{row.get('传真', '')}")
                print(f"注册地址:{row.get('注册地址', '')}")
                print(f"办公地址:{row.get('办公地址', '')}")
                print(f"邮政编码:{row.get('邮政编码', '')}")
                print(f"主营业务:{row.get('主营业务', '')}")
                print(f"经营范围:{row.get('经营范围', '')}")
                print(f"机构简介:{row.get('机构简介', '')}")

        print("\n列名:")
        print(df.columns.tolist())
        print("√ 接口测试成功\n")
    except Exception as e:
        print(f"× 接口测试失败: {e}\n")

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
        print("√ 接口测试成功\n")
    except Exception as e:
        print(f"× 接口测试失败: {e}\n")

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
        print("√ 接口测试成功\n")
    except Exception as e:
        print(f"× 接口测试失败: {e}\n")

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
        print("√ 接口测试成功\n")
    except Exception as e:
        print(f"× 接口测试失败: {e}\n")

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
        print("√ 接口测试成功\n")
    except Exception as e:
        print(f"× 接口测试失败: {e}\n")

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
        print("√ 接口测试成功\n")
    except Exception as e:
        print(f"× 接口测试失败: {e}\n")

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
        print("√ 接口测试成功\n")
    except Exception as e:
        print(f"× 接口测试失败: {e}\n")

def main():
    """主函数，执行所有测试"""
    print("开始测试akshare股票基础信息接口")
    print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("测试股票: 600030 (中信证券)")
    print()

    # # 测试所有接口
    # test_stock_individual_info_em()
    # test_stock_profile_cninfo()
    # test_stock_individual_basic_info_xq()
    # test_stock_hold_control_cninfo()
    # test_stock_ipo_summary_cninfo()
    # test_stock_register_sh()
    # test_stock_register_sz()
    # test_stock_register_bj()

    test_stock_profile_cninfo()

    print("=" * 50)
    print("所有接口测试完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()