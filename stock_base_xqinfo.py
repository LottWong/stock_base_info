#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
雪球股票基础信息获取脚本
提取指定字段并保存到文件
"""

import akshare as ak
import pandas as pd
from datetime import datetime
import os

def get_xueqiu_stock_info(stock_code="600030"):
    """
    获取雪球股票基础信息

    :param stock_code: 股票代码，默认为600030(中信证券)
    :return: 包含股票信息的字典
    """

    # 需要提取的字段列表
    required_fields = [
        'org_name_cn',           # 公司名称
        'org_short_name_cn',     # 公司简称
        'main_operation_business', # 主营业务
        'operating_scope',       # 经营范围
        'org_cn_introduction',   # 公司简介
        'legal_representative',  # 法人代表
        'general_manager',       # 总经理
        'secretary',             # 董秘
        'established_date',      # 成立日期
        'reg_asset',             # 注册资本
        'staff_num',             # 员工人数
        'org_website',           # 官方网站
        'reg_address_cn',        # 注册地址
        'office_address_cn',     # 办公地址
        'listed_date',           # 上市日期
        'provincial_name',       # 省份
        'actual_controller',     # 实际控制人
        'classi_name',           # 公司类型
        'chairman',              # 董事长
        'executives_nums',       # 高管人数
        'issue_price',           # 发行价格
        'affiliate_industry'     # 所属行业
    ]

    try:
        # 根据股票代码判断交易所前缀
        if stock_code.startswith('6'):
            # 上海证券交易所
            symbol = f"SH{stock_code}"
        elif stock_code.startswith(('0', '2', '3')):
            # 深圳证券交易所
            symbol = f"SZ{stock_code}"
        elif stock_code.startswith(('8', '4', '9')):
            # 北京证券交易所
            symbol = f"BJ{stock_code}"
        else:
            # 默认使用SH前缀
            symbol = f"SH{stock_code}"
            print(f"警告: 无法识别股票代码 {stock_code} 的交易所，默认使用SH前缀")

        print(f"正在获取雪球股票基础信息...")
        print(f"股票代码: {stock_code} ({symbol})")

        # 调用雪球API
        df = ak.stock_individual_basic_info_xq(symbol=symbol)

        if df.empty:
            print("未获取到数据")
            return None

        # 将DataFrame转换为字典，方便查找
        data_dict = dict(zip(df['item'], df['value']))

        # 提取所需字段并添加前缀
        result = {}
        for field in required_fields:
            value = data_dict.get(field, 'N/A')
            # 添加xqinfo_前缀
            result[f'xqinfo_{field}'] = value

        return result

    except KeyError as e:
        if str(e) == "'data'":
            print("× 接口调用失败: 雪球API返回数据格式异常，可能是因为:")
            print("  1. API需要认证token，当前token可能已过期")
            print("  2. 雪球网站更新了API接口")
            print("  3. 网络访问限制或防火墙问题")
            print("  建议稍后重试或使用其他数据源")
        else:
            print(f"× 数据提取错误: {e}")
        return None

    except Exception as e:
        print(f"× 接口调用失败: {e}")
        return None

def save_to_file(data, stock_code, output_file):
    """
    将股票信息保存到文件

    :param data: 股票信息字典
    :param stock_code: 股票代码
    :param output_file: 输出文件路径
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"雪球股票基础信息 (股票代码: {stock_code})\n")
            f.write(f"获取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n" + "=" * 60 + "\n")

            for key, value in data.items():
                f.write(f"{key}:{value}\n")

            f.write("=" * 60 + "\n")

    except Exception as e:
        print(f"保存文件时出错: {e}")

def main():
    """主函数"""
    print("雪球股票基础信息获取脚本")
    print("=" * 50)

    # 可以修改这里的股票代码来获取不同股票的信息
    stock_code = "600030"  # 中信证券

    # 设置输出文件路径
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'stock_base_xqinfo_output.txt')

    # 获取股票信息
    result = get_xueqiu_stock_info(stock_code)

    if result:
        # 保存到文件
        save_to_file(result, stock_code, output_file)
        print(f"\n结果已保存到: {output_file}")
        print("\n数据获取完成!")
    else:
        print("\n数据获取失败!")

if __name__ == "__main__":
    main()