#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票基础信息JSON转Markdown脚本
将 test_stock_base_info.json 转换为便于阅读的 Markdown 格式
"""

import json
from datetime import datetime
from typing import Dict, Any

# 字段中文说明映射
FIELD_NAMES = {
    # 基本字段
    'code': '股票代码',
    'name': '股票简称',
    'market': '所属市场',
    'update_time': '更新时间',
    
    # cninfo字段
    'cninfo_name': '公司全称',
    'cninfo_en_name': '英文名称',
    'cninfo_code': 'A股代码',
    'cninfo_short_name': 'A股简称',
    'cninfo_h_code': 'H股代码',
    'cninfo_h_short_name': 'H股简称',
    'cninfo_market': '所属市场',
    'cninfo_industry': '所属行业',
    'cninfo_legal_rep': '法人代表',
    'cninfo_capital': '注册资本(万元)',
    'cninfo_establish_date': '成立日期',
    'cninfo_list_date': '上市日期',
    'cninfo_website': '官方网站',
    'cninfo_reg_address': '注册地址',
    'cninfo_office_address': '办公地址',
    'cninfo_business': '主营业务',
    'cninfo_scope': '经营范围',
    'cninfo_profile': '公司简介',
    
    # xqinfo字段
    'xqinfo_org_name_cn': '公司全称',
    'xqinfo_org_short_name_cn': '公司简称',
    'xqinfo_main_operation_business': '主营业务',
    'xqinfo_operating_scope': '经营范围',
    'xqinfo_org_cn_introduction': '公司简介',
    'xqinfo_legal_representative': '法人代表',
    'xqinfo_general_manager': '总经理',
    'xqinfo_secretary': '董秘',
    'xqinfo_established_date': '成立日期',
    'xqinfo_reg_asset': '注册资本(元)',
    'xqinfo_staff_num': '员工人数',
    'xqinfo_org_website': '官方网站',
    'xqinfo_reg_address_cn': '注册地址',
    'xqinfo_office_address_cn': '办公地址',
    'xqinfo_listed_date': '上市日期',
    'xqinfo_provincial_name': '所属省份',
    'xqinfo_actual_controller': '实际控制人',
    'xqinfo_classi_name': '公司分类',
    'xqinfo_chairman': '董事长',
    'xqinfo_executives_nums': '高管人数',
    'xqinfo_issue_price': '发行价格',
    'xqinfo_affiliate_industry': '所属行业',
}

# 字段分组
BASIC_FIELDS = ['code', 'name', 'market', 'update_time']
CNINFO_FIELDS = [key for key in FIELD_NAMES.keys() if key.startswith('cninfo_')]
XQINFO_FIELDS = [key for key in FIELD_NAMES.keys() if key.startswith('xqinfo_')]


def timestamp_to_date(timestamp_ms):
    """将Unix时间戳（毫秒）转换为日期字符串"""
    if timestamp_ms is None:
        return None
    try:
        timestamp_s = timestamp_ms / 1000
        dt = datetime.fromtimestamp(timestamp_s)
        return dt.strftime('%Y-%m-%d')
    except:
        return None


def format_capital(value):
    """格式化注册资本"""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        if value >= 100000000:  # 超过1亿
            return f"{value / 10000:.2f}万元"
        else:
            return f"{value:.2f}"
    return str(value)


def format_value(value):
    """格式化字段值"""
    if value is None:
        return '-'
    if isinstance(value, dict):
        return format_dict(value)
    if isinstance(value, (list, tuple)):
        return ', '.join(map(str, value))
    if isinstance(value, float):
        # 如果是整数部分显示为整数
        if value.is_integer():
            return str(int(value))
        return str(value)
    return str(value)


def format_dict(d):
    """格式化字典对象"""
    if not d:
        return '-'
    return ', '.join(f"{k}: {v}" for k, v in d.items())


def generate_stock_md(stock_code, stock_data):
    """生成单个股票的Markdown内容"""
    md = []
    md.append(f"## {stock_data.get('name', '')} ({stock_code})")
    md.append("")
    
    # 基本字段
    md.append("### 基本信息")
    md.append("")
    for field in BASIC_FIELDS:
        if field in stock_data:
            cn_name = FIELD_NAMES.get(field, field)
            value = format_value(stock_data[field])
            md.append(f"- **{cn_name}**: {value}")
    md.append("")
    
    # cninfo字段
    md.append("### 巨潮资讯数据")
    md.append("")
    for field in CNINFO_FIELDS:
        if field in stock_data and stock_data[field] is not None:
            cn_name = FIELD_NAMES.get(field, field)
            value = format_value(stock_data[field])
            md.append(f"- **{cn_name}**: {value}")
    md.append("")
    
    # xqinfo字段
    md.append("### 雪球数据")
    md.append("")
    
    # 先处理常规字段
    for field in XQINFO_FIELDS:
        if field == 'xqinfo_affiliate_industry':
            continue
        if field in stock_data and stock_data[field] is not None:
            cn_name = FIELD_NAMES.get(field, field)
            value = stock_data[field]
            
            # 特殊处理时间戳字段
            if field in ['xqinfo_established_date', 'xqinfo_listed_date']:
                value = timestamp_to_date(value)
            
            # 特殊处理注册资本
            elif field == 'xqinfo_reg_asset':
                value = format_capital(value)
            
            if value is not None:
                md.append(f"- **{cn_name}**: {format_value(value)}")
    
    # 处理行业信息
    if 'xqinfo_affiliate_industry' in stock_data and stock_data['xqinfo_affiliate_industry']:
        industry = stock_data['xqinfo_affiliate_industry']
        if isinstance(industry, dict):
            md.append(f"- **所属行业**: {industry.get('ind_name', '')} ({industry.get('ind_code', '')})")
    
    md.append("")
    md.append("---")
    md.append("")
    
    return '\n'.join(md)


def json_to_markdown(json_file, output_file):
    """将JSON文件转换为Markdown文件"""
    print(f"正在读取 {json_file}...")
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"成功读取 {len(data)} 只股票的数据")
        
        # 生成Markdown内容
        md_content = []
        md_content.append("# 股票基础信息汇总")
        md_content.append("")
        md_content.append(f"本文档包含 {len(data)} 只股票的基础信息。")
        md_content.append("")
        md_content.append("---")
        md_content.append("")
        
        # 按股票代码排序
        sorted_codes = sorted(data.keys())
        
        print("正在生成Markdown内容...")
        for idx, code in enumerate(sorted_codes, 1):
            print(f"处理进度: {idx}/{len(sorted_codes)} - {code}")
            md_content.append(generate_stock_md(code, data[code]))
        
        # 写入文件
        print(f"正在写入文件 {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md_content))
        
        print(f"成功生成Markdown文件: {output_file}")
        return True
        
    except FileNotFoundError:
        print(f"错误: 文件 {json_file} 不存在")
        return False
    except json.JSONDecodeError as e:
        print(f"错误: JSON格式错误 - {e}")
        return False
    except Exception as e:
        print(f"错误: {e}")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("股票基础信息JSON转Markdown工具")
    print("=" * 60)
    print()
    
    # 文件路径
    json_file = "stock_base_info.json"
    output_file = "./data/stock_base_info.md"
    
    # 执行转换
    json_to_markdown(json_file, output_file)
    
    print()
    print("=" * 60)
    print("处理完成")
    print("=" * 60)


if __name__ == "__main__":
    main()

