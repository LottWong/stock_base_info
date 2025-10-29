#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票基础信息Markdown文档拆分工具

将包含所有股票信息的单个Markdown文件拆分为按股票分类的独立文件
"""

import os
import re
from pathlib import Path


def split_stock_md_file(input_file, output_dir):
    """
    拆分股票Markdown文件

    Args:
        input_file (str): 输入的股票汇总文件路径
        output_dir (str): 输出目录路径
    """
    # 确保输出目录存在
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # 读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式匹配每个股票的信息块
    # 匹配以 ## 开头，后面跟着股票名和股票代码的行
    pattern = r'(##\s+([^(\n]+)\s*\((\d+)\)\s*\n.*?)(?=##\s+[^(\n]+\s*\(\d+\)|\Z)'

    # 找到所有匹配的股票信息块
    matches = re.findall(pattern, content, re.DOTALL)

    print(f"找到 {len(matches)} 只股票")

    split_count = 0

    for match in matches:
        full_content, stock_name, stock_code = match

        # 清理股票名称，去除多余空格和特殊字符
        clean_name = stock_name.strip().replace(' ', '').replace('\n', '')

        # 清理文件名中的特殊字符，只保留字母、数字、中文
        import unicodedata
        def clean_filename(name):
            result = ""
            for char in name:
                # 保留中文字符、英文字母、数字
                if ('\u4e00' <= char <= '\u9fff' or  # 中文
                    'a' <= char <= 'z' or 'A' <= char <= 'Z' or  # 英文
                    '0' <= char <= '9'):  # 数字
                    result += char
                # 特殊处理一些常见字符
                elif char in 'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ':
                    result += char
                elif char == '科':
                    result += char
                elif char == 'Ａ':
                    result += 'A'
                elif char == 'Ｂ':
                    result += 'B'
                # 其他特殊字符替换为下划线
                else:
                    result += '_'
            return result

        clean_name = clean_filename(clean_name)

        # 生成文件名：股票代码_股票名.md
        filename = f"{stock_code}_{clean_name}.md"
        filepath = os.path.join(output_dir, filename)

        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content.strip())

        print(f"已生成: {filename}")
        split_count += 1

    print(f"\n拆分完成！共生成 {split_count} 个文件")
    return split_count


def main():
    """主函数"""
    # 文件路径配置
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "data", "stock_base_info.md")
    output_dir = os.path.join(current_dir, "data", "items")

    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误: 输入文件不存在 - {input_file}")
        return

    # 执行拆分
    try:
        count = split_stock_md_file(input_file, output_dir)
        print(f"\n成功拆分 {count} 只股票信息到 {output_dir}")
    except Exception as e:
        print(f"拆分过程中出现错误: {str(e)}")


if __name__ == "__main__":
    main()