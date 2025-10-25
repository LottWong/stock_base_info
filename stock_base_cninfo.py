#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用akshare获取股票基础信息（巨潮资讯公司概况）
通过stock_profile_cninfo接口获取股票信息并保存指定字段
"""

import akshare as ak
import pandas as pd
from datetime import datetime

# 设置pandas显示选项，显示完整内容
pd.set_option('display.max_columns', None)      # 显示所有列
pd.set_option('display.max_rows', None)         # 显示所有行
pd.set_option('display.width', None)           # 不限制列宽
pd.set_option('display.max_colwidth', None)     # 不限制列内容宽度
pd.set_option('expand_frame_repr', False)  # 不换行显示

def get_stock_basic_info(symbol):
    """
    获取股票基础信息

    参数:
        symbol (str): 股票代码，如"600030"

    返回:
        tuple: (cn_dict, en_dict) 两种字典格式
            cn_dict: 包含股票基础信息的中文键名字典
            en_dict: 包含股票基础信息的英文键名字典（以cninfo_开头）
            如果获取失败则返回(None, None)
    """
    try:
        # 调用akshare接口获取股票信息
        df = ak.stock_profile_cninfo(symbol=symbol)

        if df.empty:
            print(f"未找到股票代码 {symbol} 的信息")
            return None, None

        # 提取所需字段
        cn_stock_info = {}
        en_stock_info = {}
        if not df.empty:
            row = df.iloc[0]  # 取第一行数据

            # 中文键名字典
            cn_stock_info['公司名称'] = row.get('公司名称', '')
            cn_stock_info['英文名称'] = row.get('英文名称', '')
            cn_stock_info['A股代码'] = row.get('A股代码', '')
            cn_stock_info['A股简称'] = row.get('A股简称', '')
            cn_stock_info['H股代码'] = row.get('H股代码', '')
            cn_stock_info['H股简称'] = row.get('H股简称', '')
            cn_stock_info['所属市场'] = row.get('所属市场', '')
            cn_stock_info['所属行业'] = row.get('所属行业', '')
            cn_stock_info['法人代表'] = row.get('法人代表', '')
            cn_stock_info['注册资金'] = row.get('注册资金', '')
            cn_stock_info['成立日期'] = row.get('成立日期', '')
            cn_stock_info['上市日期'] = row.get('上市日期', '')
            cn_stock_info['官方网站'] = row.get('官方网站', '')
            cn_stock_info['注册地址'] = row.get('注册地址', '')
            cn_stock_info['办公地址'] = row.get('办公地址', '')
            cn_stock_info['主营业务'] = row.get('主营业务', '')
            cn_stock_info['经营范围'] = row.get('经营范围', '')
            cn_stock_info['机构简介'] = row.get('机构简介', '')

            # 英文键名字典（以cninfo_开头）
            en_stock_info['cninfo_name'] = row.get('公司名称', '')
            en_stock_info['cninfo_en_name'] = row.get('英文名称', '')
            en_stock_info['cninfo_code'] = row.get('A股代码', '')
            en_stock_info['cninfo_short_name'] = row.get('A股简称', '')
            en_stock_info['cninfo_h_code'] = row.get('H股代码', '')
            en_stock_info['cninfo_h_short_name'] = row.get('H股简称', '')
            en_stock_info['cninfo_market'] = row.get('所属市场', '')
            en_stock_info['cninfo_industry'] = row.get('所属行业', '')
            en_stock_info['cninfo_legal_rep'] = row.get('法人代表', '')
            en_stock_info['cninfo_capital'] = row.get('注册资金', '')
            en_stock_info['cninfo_establish_date'] = row.get('成立日期', '')
            en_stock_info['cninfo_list_date'] = row.get('上市日期', '')
            en_stock_info['cninfo_website'] = row.get('官方网站', '')
            en_stock_info['cninfo_reg_address'] = row.get('注册地址', '')
            en_stock_info['cninfo_office_address'] = row.get('办公地址', '')
            en_stock_info['cninfo_business'] = row.get('主营业务', '')
            en_stock_info['cninfo_scope'] = row.get('经营范围', '')
            en_stock_info['cninfo_profile'] = row.get('机构简介', '')

        return cn_stock_info, en_stock_info

    except Exception as e:
        print(f"获取股票 {symbol} 信息时出错: {e}")
        return None, None

def print_stock_info(stock_info):
    """
    打印股票信息

    参数:
        stock_info (dict): 股票信息字典
    """
    if not stock_info:
        print("股票信息为空")
        return

    print("=" * 60)
    print("股票基础信息")
    print("=" * 60)

    # 按照指定格式显示
    print(f"公司名称:{stock_info.get('公司名称', '')}")
    print(f"英文名称:{stock_info.get('英文名称', '')}")
    print(f"A股代码:{stock_info.get('A股代码', '')}")
    print(f"A股简称:{stock_info.get('A股简称', '')}")
    print(f"H股代码:{stock_info.get('H股代码', '')}")
    print(f"H股简称:{stock_info.get('H股简称', '')}")
    print(f"所属市场:{stock_info.get('所属市场', '')}")
    print(f"所属行业:{stock_info.get('所属行业', '')}")
    print(f"法人代表:{stock_info.get('法人代表', '')}")
    print(f"注册资金:{stock_info.get('注册资金', '')}")
    print(f"成立日期:{stock_info.get('成立日期', '')}")
    print(f"上市日期:{stock_info.get('上市日期', '')}")
    print(f"官方网站:{stock_info.get('官方网站', '')}")
    print(f"注册地址:{stock_info.get('注册地址', '')}")
    print(f"办公地址:{stock_info.get('办公地址', '')}")
    print(f"主营业务:{stock_info.get('主营业务', '')}")
    print(f"经营范围:{stock_info.get('经营范围', '')}")
    print(f"机构简介:{stock_info.get('机构简介', '')}")
    print("=" * 60)

def print_en_stock_info(en_stock_info):
    """
    打印英文键名格式的股票信息

    参数:
        en_stock_info (dict): 英文键名的股票信息字典
    """
    if not en_stock_info:
        print("股票信息为空")
        return

    print("=" * 60)
    print("Stock Basic Info (English Keys)")
    print("=" * 60)

    # 按照指定格式显示
    print(f"cninfo_name:{en_stock_info.get('cninfo_name', '')}")
    print(f"cninfo_en_name:{en_stock_info.get('cninfo_en_name', '')}")
    print(f"cninfo_code:{en_stock_info.get('cninfo_code', '')}")
    print(f"cninfo_short_name:{en_stock_info.get('cninfo_short_name', '')}")
    print(f"cninfo_h_code:{en_stock_info.get('cninfo_h_code', '')}")
    print(f"cninfo_h_short_name:{en_stock_info.get('cninfo_h_short_name', '')}")
    print(f"cninfo_market:{en_stock_info.get('cninfo_market', '')}")
    print(f"cninfo_industry:{en_stock_info.get('cninfo_industry', '')}")
    print(f"cninfo_legal_rep:{en_stock_info.get('cninfo_legal_rep', '')}")
    print(f"cninfo_capital:{en_stock_info.get('cninfo_capital', '')}")
    print(f"cninfo_establish_date:{en_stock_info.get('cninfo_establish_date', '')}")
    print(f"cninfo_list_date:{en_stock_info.get('cninfo_list_date', '')}")
    print(f"cninfo_website:{en_stock_info.get('cninfo_website', '')}")
    print(f"cninfo_reg_address:{en_stock_info.get('cninfo_reg_address', '')}")
    print(f"cninfo_office_address:{en_stock_info.get('cninfo_office_address', '')}")
    print(f"cninfo_business:{en_stock_info.get('cninfo_business', '')}")
    print(f"cninfo_scope:{en_stock_info.get('cninfo_scope', '')}")
    print(f"cninfo_profile:{en_stock_info.get('cninfo_profile', '')}")
    print("=" * 60)

def save_stock_info_to_file(cn_stock_info, en_stock_info, symbol):
    """
    将股票信息保存到文件

    参数:
        cn_stock_info (dict): 中文键名的股票信息字典
        en_stock_info (dict): 英文键名的股票信息字典
        symbol (str): 股票代码
    """
    if not cn_stock_info or not en_stock_info:
        return

    # 创建输出目录
    output_dir = "output"
    try:
        import os
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    except Exception as e:
        print(f"创建输出目录失败: {e}")
        output_dir = "."

    # 生成文件名
    cn_filename = f"{output_dir}/stock_base_cninfo_output.txt"
    en_filename = f"{output_dir}/stock_base_cninfo_en_output.txt"

    try:
        # 保存中文键名格式
        with open(cn_filename, 'w', encoding='utf-8') as f:
            f.write(f"股票基础信息 (股票代码: {symbol})\n")
            f.write(f"获取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n")
            f.write("=" * 60 + "\n")

            # 写入中文股票信息
            for key, value in cn_stock_info.items():
                f.write(f"{key}:{value}\n")

            f.write("=" * 60 + "\n")

        print(f"中文键名股票信息已保存到: {cn_filename}")

        # 保存英文键名格式
        with open(en_filename, 'w', encoding='utf-8') as f:
            f.write(f"Stock Basic Info (Stock Code: {symbol})\n")
            f.write(f"Get Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n")
            f.write("=" * 60 + "\n")

            # 写入英文股票信息
            for key, value in en_stock_info.items():
                f.write(f"{key}:{value}\n")

            f.write("=" * 60 + "\n")

        print(f"英文键名股票信息已保存到: {en_filename}")

    except Exception as e:
        print(f"保存文件时出错: {e}")

def main():
    """
    主函数
    """
    # 测试用股票代码
    stock_symbol = "600030"  # 中信证券

    print(f"开始获取股票 {stock_symbol} 的基础信息...")
    print(f"获取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 获取股票信息（返回两种格式）
    cn_stock_info, en_stock_info = get_stock_basic_info(stock_symbol)

    if cn_stock_info and en_stock_info:
        # 打印中文键名信息到控制台
        print_stock_info(cn_stock_info)

        print("\n")

        # 打印英文键名信息到控制台
        print_en_stock_info(en_stock_info)

        # 保存两种格式到文件
        save_stock_info_to_file(cn_stock_info, en_stock_info, stock_symbol)
    else:
        print(f"获取股票 {stock_symbol} 信息失败")

if __name__ == "__main__":
    main()
