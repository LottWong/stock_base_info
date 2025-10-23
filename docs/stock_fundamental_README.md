# AkShare Stock_Fundamental 模块说明文档

## 概述

本文档详细描述了 AkShare 股票基本面（stock_fundamental）模块下各个脚本文件及其提供的接口功能。该模块专注于股票的基本面数据分析，包含**51个函数接口**，涵盖19个脚本文件，提供从财务报表到公司治理的全方位基本面数据服务。

## 模块特点

- **基本面专精**: 专注于股票基本面数据，涵盖财务、治理、预测等各个维度
- **多市场覆盖**: 支持A股、港股、美股的基本面数据获取
- **权威数据源**: 整合新浪财经、东方财富、同花顺、雪球等权威数据源
- **深度分析**: 提供财务报表、业绩预测、机构持股、限售解禁等深度数据
- **注册制追踪**: 实时跟踪科创板、创业板注册制审核进展

## 目录结构

```
stock_fundamental/
├── __init__.py                           # 模块初始化文件
├── stock_finance_sina.py                # 新浪财经财务数据（核心）
├── stock_register_em.py                 # 东方财富注册制审核
├── stock_finance_ths.py                 # 同花顺财务数据
├── stock_restricted_em.py               # 限售股解禁数据
├── stock_profit_forecast_em.py          # 业绩预测数据
├── stock_finance_hk_em.py               # 港股财务数据
├── stock_finance_us_em.py               # 美股财务数据
├── stock_hold.py                        # 机构持股数据
├── stock_basic_info_xq.py               # 雪球基本信息
└── ... (其他脚本文件)
```

## 模块分类

### 📊 财务报表数据 (Financial Reports)
- **三大报表**: 资产负债表、利润表、现金流量表
- **财务指标**: ROE、ROA、毛利率等关键指标
- **财务摘要**: 核心财务数据汇总
- **多市场支持**: A股、港股、美股财务数据

### 🔮 业绩预测分析 (Earnings Forecast)
- **业绩预测**: 券商研究报告的业绩预测
- **盈利预测**: EPS、营收增长预测
- **评级推荐**: 买入、持有、卖出评级
- **目标价格**: 分析师目标价预测

### 🏛️ 公司治理数据 (Corporate Governance)
- **机构持股**: 基金、保险等机构持股情况
- **限售解禁**: 限售股解禁时间表和规模
- **股本结构**: 总股本、流通股本变化
- **公司公告**: 重要公告和信息披露

### 🆕 新股发行数据 (IPO & Registration)
- **注册制审核**: 科创板、创业板注册制进展
- **IPO申报**: 新股申报和审核状态
- **发行信息**: 发行价格、发行规模
- **上市进程**: 从申报到上市的全流程跟踪

### 📈 估值分析数据 (Valuation Analysis)
- **估值指标**: PE、PB、PS等估值倍数
- **行业比较**: 同行业估值水平对比
- **历史估值**: 估值水平的历史变化
- **合理价值**: 基于基本面的合理价值评估

## 主要脚本文件详细说明

### 1. stock_finance_sina.py - 新浪财经财务数据（核心模块）

**功能描述**: 新浪财经财务数据的核心获取模块，提供最全面的A股财务数据。

**接口数量**: 12个函数

**主要接口**:

#### `stock_financial_report_sina(stock, symbol) -> pd.DataFrame`
- **功能**: 获取三大财务报表数据
- **参数**: 
  - `stock`: 股票代码，如 "sh600600"
  - `symbol`: 报表类型，可选 "资产负债表", "利润表", "现金流量表"
- **返回**: 指定报表的历年数据
- **特点**: 数据完整，支持多年度对比

#### `stock_financial_abstract(symbol) -> pd.DataFrame`
- **功能**: 获取财务报表关键指标
- **参数**: `symbol` - 股票代码
- **返回**: 关键财务指标汇总
- **包含指标**: ROE、ROA、毛利率、净利率、资产负债率等

#### `stock_financial_analysis_indicator(symbol) -> pd.DataFrame`
- **功能**: 获取财务分析指标
- **返回**: 详细的财务分析指标数据
- **应用**: 深度财务分析和投资决策

#### `stock_add_stock(symbol) -> pd.DataFrame`
- **功能**: 获取增发股票信息
- **返回**: 股票增发的历史记录

#### `stock_xjll_em(date) -> pd.DataFrame`
- **功能**: 获取现金流量表数据
- **参数**: `date` - 报告期日期
- **返回**: 指定期间的现金流量表数据

### 2. stock_register_em.py - 注册制审核数据

**功能描述**: 跟踪科创板、创业板、北交所注册制审核进展。

**接口数量**: 6个函数

**主要接口**:

#### `stock_register_kcb() -> pd.DataFrame`
- **功能**: 获取科创板注册制审核信息
- **返回字段**:
  - 企业名称、最新状态、注册地
  - 行业、保荐机构、律师事务所
  - 会计师事务所、更新日期、受理日期
  - 招股说明书链接
- **应用**: 科创板投资机会发现

#### `stock_register_cyb() -> pd.DataFrame`
- **功能**: 获取创业板注册制审核信息
- **特点**: 与科创板格式一致，便于对比分析

#### `stock_register_bj() -> pd.DataFrame`
- **功能**: 获取北交所注册制审核信息
- **特点**: 北交所专属数据，关注中小企业

#### `stock_register_db() -> pd.DataFrame`
- **功能**: 获取主板注册制审核信息
- **特点**: 主板注册制改革后的审核数据

### 3. stock_finance_ths.py - 同花顺财务数据

**功能描述**: 同花顺财务指标数据，提供标准化的财务分析。

**接口数量**: 6个函数

**主要接口**:

#### `stock_financial_abstract_ths(symbol, indicator) -> pd.DataFrame`
- **功能**: 获取主要财务指标
- **参数**:
  - `symbol`: 股票代码
  - `indicator`: 可选 "按报告期", "按年度", "按单季度"
- **特点**: 数据标准化程度高，便于量化分析

#### `stock_financial_debt_ths(symbol, indicator) -> pd.DataFrame`
- **功能**: 获取资产负债表数据
- **特点**: 同花顺标准化格式

#### `stock_financial_benefit_ths(symbol, indicator) -> pd.DataFrame`
- **功能**: 获取利润表数据
- **应用**: 盈利能力分析

#### `stock_financial_cash_ths(symbol, indicator) -> pd.DataFrame`
- **功能**: 获取现金流量表数据
- **应用**: 现金流分析

### 4. stock_restricted_em.py - 限售股解禁数据

**功能描述**: 限售股解禁时间表和影响分析。

**接口数量**: 4个函数

**主要接口**:

#### `stock_restricted_release_summary_em(symbol, start_date, end_date) -> pd.DataFrame`
- **功能**: 获取限售股解禁汇总数据
- **参数**:
  - `symbol`: 市场类型，如 "全部股票", "沪市A股"
  - `start_date`, `end_date`: 时间范围
- **返回字段**:
  - 解禁时间、当日解禁股票家数
  - 解禁数量、实际解禁数量
  - 实际解禁市值、市场指数表现

#### `stock_restricted_release_detail_em(start_date, end_date) -> pd.DataFrame`
- **功能**: 获取限售股解禁详细数据
- **应用**: 个股解禁压力分析

### 5. stock_profit_forecast_em.py - 业绩预测数据

**功能描述**: 券商研究报告中的业绩预测数据。

**主要接口**:

#### `stock_profit_forecast_em(symbol) -> pd.DataFrame`
- **功能**: 获取盈利预测数据
- **参数**: `symbol` - 行业板块名称（可选）
- **返回字段**:
  - 股票代码、名称、最新评级
  - 机构数量、买入家数、增持家数
  - 中性家数、减持家数、卖出家数
  - 目标价、最新价、目标涨幅
  - 预测年度、预测EPS

### 6. stock_finance_hk_em.py - 港股财务数据

**功能描述**: 港股上市公司的财务报表数据。

**接口数量**: 2个函数

**主要接口**:

#### `stock_financial_hk_report_em(stock, symbol, indicator) -> pd.DataFrame`
- **功能**: 获取港股三大财务报表
- **参数**:
  - `stock`: 港股代码，如 "00700"
  - `symbol`: 报表类型
  - `indicator`: "年度" 或 "报告期"
- **特点**: 港股财务数据格式化处理

### 7. stock_finance_us_em.py - 美股财务数据

**功能描述**: 美股上市公司的财务报表数据。

**接口数量**: 4个函数

**主要接口**:

#### `stock_financial_us_report_em(stock, symbol, indicator) -> pd.DataFrame`
- **功能**: 获取美股财务报表
- **参数**:
  - `stock`: 美股代码，如 "TSLA"
  - `symbol`: 报表类型
  - `indicator`: 报告期类型
- **特点**: 美股GAAP会计准则数据

### 8. stock_hold.py - 机构持股数据

**功能描述**: 机构投资者持股情况分析。

**接口数量**: 2个函数

**主要接口**:

#### `stock_institute_hold(symbol) -> pd.DataFrame`
- **功能**: 获取机构持股一览表
- **参数**: `symbol` - 报告期，如 "20191"（2019年一季报）
- **返回字段**:
  - 证券代码、证券简称
  - 机构数、机构数变化
  - 持股比例、持股比例增幅
  - 占流通股比例、占流通股比例增幅

### 9. stock_basic_info_xq.py - 雪球基本信息

**功能描述**: 雪球平台的公司基本信息数据。

**接口数量**: 3个函数

**主要接口**:

#### `stock_individual_basic_info_xq(symbol, token) -> pd.DataFrame`
- **功能**: 获取A股公司基本信息
- **参数**: 
  - `symbol`: 股票代码
  - `token`: 雪球token（可选）
- **返回**: 公司简介、基本信息

#### `stock_individual_basic_info_us_xq(symbol, token) -> pd.DataFrame`
- **功能**: 获取美股公司基本信息
- **特点**: 美股公司详细资料

### 10. 其他重要脚本文件

#### stock_profit_forecast_ths.py - 同花顺业绩预测
- **功能**: 同花顺平台的业绩预测数据

#### stock_profit_forecast_hk_etnet.py - 港股业绩预测
- **功能**: 港股业绩预测数据

#### stock_recommend.py - 投资评级推荐
- **功能**: 券商投资评级和推荐数据

#### stock_notice.py - 公司公告
- **功能**: 上市公司重要公告信息

#### stock_ipo_declare.py - IPO申报
- **功能**: 新股IPO申报信息

#### stock_gbjg_em.py - 股本结构
- **功能**: 股本结构变化数据

## 使用示例

### 1. 财务报表数据获取

```python
import akshare as ak

# 获取资产负债表
df_balance = ak.stock_financial_report_sina(stock="sh600519", symbol="资产负债表")
print("资产负债表数据:")
print(df_balance.head())

# 获取利润表
df_profit = ak.stock_financial_report_sina(stock="sh600519", symbol="利润表")
print("利润表数据:")
print(df_profit.head())

# 获取现金流量表
df_cash = ak.stock_financial_report_sina(stock="sh600519", symbol="现金流量表")
print("现金流量表数据:")
print(df_cash.head())

# 获取财务关键指标
df_abstract = ak.stock_financial_abstract(symbol="600519")
print("财务关键指标:")
print(df_abstract.head())
```

### 2. 注册制审核数据

```python
# 科创板注册制审核
df_kcb = ak.stock_register_kcb()
print(f"科创板审核企业数量: {len(df_kcb)}")
print(df_kcb[['企业名称', '最新状态', '行业']].head())

# 创业板注册制审核
df_cyb = ak.stock_register_cyb()
print(f"创业板审核企业数量: {len(df_cyb)}")

# 筛选已通过审核的企业
approved_companies = df_kcb[df_kcb['最新状态'].str.contains('通过', na=False)]
print(f"已通过审核企业: {len(approved_companies)}")
```

### 3. 同花顺财务数据

```python
# 获取主要财务指标（按报告期）
df_ths_abstract = ak.stock_financial_abstract_ths(symbol="000063", indicator="按报告期")
print("同花顺财务指标:")
print(df_ths_abstract.head())

# 获取资产负债表
df_ths_debt = ak.stock_financial_debt_ths(symbol="000063", indicator="按年度")
print("同花顺资产负债表:")
print(df_ths_debt.head())

# 获取利润表
df_ths_benefit = ak.stock_financial_benefit_ths(symbol="000063", indicator="按报告期")
print("同花顺利润表:")
print(df_ths_benefit.head())
```

### 4. 限售股解禁数据

```python
# 获取限售股解禁汇总
df_restricted = ak.stock_restricted_release_summary_em(
    symbol="全部股票", 
    start_date="20240301", 
    end_date="20240331"
)
print("3月份限售股解禁情况:")
print(df_restricted.head())

# 分析解禁规模
total_release_value = df_restricted['实际解禁市值'].sum()
print(f"3月份总解禁市值: {total_release_value/10000:.2f} 亿元")
```

### 5. 业绩预测数据

```python
# 获取全市场盈利预测
df_forecast = ak.stock_profit_forecast_em()
print("盈利预测数据:")
print(df_forecast[['股票简称', '最新评级', '机构数量', '目标价', '目标涨幅']].head())

# 筛选买入评级较多的股票
buy_stocks = df_forecast[df_forecast['买入家数'] >= 5]
print(f"买入评级≥5家的股票数量: {len(buy_stocks)}")
```

### 6. 港股和美股财务数据

```python
# 港股财务数据
df_hk = ak.stock_financial_hk_report_em(stock="00700", symbol="利润表", indicator="年度")
print("腾讯港股利润表:")
print(df_hk.head())

# 美股财务数据
df_us = ak.stock_financial_us_report_em(stock="TSLA", symbol="综合损益表", indicator="年报")
print("特斯拉美股财务数据:")
print(df_us.head())
```

### 7. 机构持股分析

```python
# 获取机构持股数据
df_institute = ak.stock_institute_hold(symbol="20241")  # 2024年一季报
print("机构持股数据:")
print(df_institute.head())

# 分析机构持股集中度
high_institution = df_institute[df_institute['机构数'] >= 50]
print(f"机构持股数量≥50的股票: {len(high_institution)}")
```

### 8. 综合基本面分析示例

```python
def comprehensive_fundamental_analysis(symbol="600519"):
    """综合基本面分析"""
    
    print(f"=== {symbol} 综合基本面分析 ===")
    
    # 1. 财务报表分析
    try:
        df_abstract = ak.stock_financial_abstract(symbol=symbol)
        print("1. 财务关键指标:")
        if not df_abstract.empty:
            latest_roe = df_abstract.iloc[-1].get('净资产收益率', 'N/A')
            print(f"   最新ROE: {latest_roe}")
    except Exception as e:
        print(f"   财务数据获取失败: {e}")
    
    # 2. 业绩预测分析
    try:
        df_forecast = ak.stock_profit_forecast_em()
        stock_forecast = df_forecast[df_forecast['股票代码'] == symbol]
        if not stock_forecast.empty:
            print("2. 业绩预测:")
            print(f"   机构覆盖数量: {stock_forecast.iloc[0]['机构数量']}")
            print(f"   目标价: {stock_forecast.iloc[0]['目标价']}")
            print(f"   最新评级: {stock_forecast.iloc[0]['最新评级']}")
    except Exception as e:
        print(f"   业绩预测获取失败: {e}")
    
    # 3. 机构持股分析
    try:
        df_institute = ak.stock_institute_hold(symbol="20241")
        stock_institute = df_institute[df_institute['证券代码'] == symbol]
        if not stock_institute.empty:
            print("3. 机构持股:")
            print(f"   机构数量: {stock_institute.iloc[0]['机构数']}")
            print(f"   持股比例: {stock_institute.iloc[0]['持股比例']}%")
    except Exception as e:
        print(f"   机构持股数据获取失败: {e}")
    
    return True

# 使用示例
comprehensive_fundamental_analysis("600519")
```

## 高级应用场景

### 1. 基本面选股策略

```python
def fundamental_stock_screening():
    """基于基本面的股票筛选"""
    
    # 获取业绩预测数据
    df_forecast = ak.stock_profit_forecast_em()
    
    # 筛选条件
    conditions = (
        (df_forecast['机构数量'] >= 10) &          # 机构覆盖数量≥10
        (df_forecast['买入家数'] >= 5) &           # 买入评级≥5家
        (df_forecast['目标涨幅'] >= 20)            # 目标涨幅≥20%
    )
    
    selected_stocks = df_forecast[conditions]
    
    print(f"筛选出 {len(selected_stocks)} 只股票")
    print(selected_stocks[['股票简称', '机构数量', '买入家数', '目标涨幅']].head(10))
    
    return selected_stocks

# 执行筛选
selected = fundamental_stock_screening()
```

### 2. 注册制投资机会分析

```python
def registration_investment_analysis():
    """注册制投资机会分析"""
    
    # 获取各板块注册制数据
    kcb_data = ak.stock_register_kcb()
    cyb_data = ak.stock_register_cyb()
    
    # 分析各行业申报情况
    kcb_industry = kcb_data['行业'].value_counts()
    cyb_industry = cyb_data['行业'].value_counts()
    
    print("科创板申报行业分布:")
    print(kcb_industry.head(10))
    
    print("\n创业板申报行业分布:")
    print(cyb_industry.head(10))
    
    # 分析审核进度
    kcb_status = kcb_data['最新状态'].value_counts()
    print("\n科创板审核状态分布:")
    print(kcb_status)
    
    return kcb_data, cyb_data

# 执行分析
kcb, cyb = registration_investment_analysis()
```

### 3. 限售解禁影响分析

```python
def restriction_release_impact_analysis(start_date="20240301", end_date="20240331"):
    """限售解禁影响分析"""
    
    # 获取解禁数据
    df_release = ak.stock_restricted_release_summary_em(
        symbol="全部股票", 
        start_date=start_date, 
        end_date=end_date
    )
    
    # 分析解禁规模
    total_release_count = df_release['当日解禁股票家数'].sum()
    total_release_value = df_release['实际解禁市值'].sum()
    
    print(f"解禁分析 ({start_date} - {end_date}):")
    print(f"解禁股票总数: {total_release_count} 只")
    print(f"解禁市值总额: {total_release_value/10000:.2f} 亿元")
    
    # 分析与市场表现的关系
    avg_index_change = df_release['沪深300指数涨跌幅'].mean()
    print(f"期间沪深300平均涨跌幅: {avg_index_change:.2f}%")
    
    # 找出解禁压力最大的日期
    max_release_date = df_release.loc[df_release['实际解禁市值'].idxmax(), '解禁时间']
    max_release_value = df_release['实际解禁市值'].max()
    
    print(f"解禁压力最大日期: {max_release_date}")
    print(f"单日最大解禁市值: {max_release_value/10000:.2f} 亿元")
    
    return df_release

# 执行分析
release_analysis = restriction_release_impact_analysis()
```

### 4. 多市场财务对比分析

```python
def multi_market_financial_comparison():
    """多市场财务数据对比分析"""
    
    # A股数据（以贵州茅台为例）
    try:
        a_stock_data = ak.stock_financial_abstract(symbol="600519")
        print("A股财务数据获取成功")
    except Exception as e:
        print(f"A股数据获取失败: {e}")
        a_stock_data = None
    
    # 港股数据（以腾讯为例）
    try:
        hk_stock_data = ak.stock_financial_hk_report_em(
            stock="00700", 
            symbol="利润表", 
            indicator="年度"
        )
        print("港股财务数据获取成功")
    except Exception as e:
        print(f"港股数据获取失败: {e}")
        hk_stock_data = None
    
    # 美股数据（以特斯拉为例）
    try:
        us_stock_data = ak.stock_financial_us_report_em(
            stock="TSLA", 
            symbol="综合损益表", 
            indicator="年报"
        )
        print("美股财务数据获取成功")
    except Exception as e:
        print(f"美股数据获取失败: {e}")
        us_stock_data = None
    
    return {
        'A股': a_stock_data,
        '港股': hk_stock_data,
        '美股': us_stock_data
    }

# 执行对比分析
market_comparison = multi_market_financial_comparison()
```

## 数据质量和注意事项

### 1. 数据时效性
- **财务数据**: 季报发布后1-2个工作日更新
- **注册制数据**: 实时更新审核进展
- **业绩预测**: 研究报告发布后及时更新
- **限售解禁**: 提前公布解禁时间表

### 2. 数据完整性
- **A股数据**: 覆盖沪深京三个交易所
- **港股数据**: 覆盖主要港股上市公司
- **美股数据**: 覆盖主要美股上市公司
- **历史数据**: 财务数据可追溯到2007年

### 3. 数据准确性
- **官方来源**: 优先使用交易所和监管机构数据
- **权威媒体**: 新浪财经、东方财富等权威财经媒体
- **交叉验证**: 多数据源交叉验证确保准确性
- **及时更正**: 发现数据错误及时更正

### 4. 使用限制
- **访问频率**: 建议单个接口调用间隔不少于1秒
- **数据量限制**: 单次获取建议不超过5000条记录
- **Token要求**: 雪球数据需要有效的token
- **网络稳定**: 确保网络连接稳定

## 错误处理和最佳实践

### 1. 错误处理示例

```python
import akshare as ak
import pandas as pd
import time

def safe_financial_data_fetch(symbol, max_retries=3):
    """安全的财务数据获取"""
    
    for attempt in range(max_retries):
        try:
            # 尝试获取财务摘要
            df_abstract = ak.stock_financial_abstract(symbol=symbol)
            if not df_abstract.empty:
                return df_abstract
            else:
                print(f"获取到空数据，第{attempt+1}次重试...")
                
        except Exception as e:
            print(f"数据获取失败 (尝试 {attempt+1}/{max_retries}): {e}")
            
        if attempt < max_retries - 1:
            time.sleep(2)  # 等待2秒后重试
    
    print(f"经过{max_retries}次重试仍然失败")
    return pd.DataFrame()

# 使用示例
df = safe_financial_data_fetch("600519")
```

### 2. 数据缓存策略

```python
import pickle
import os
from datetime import datetime, timedelta

def cached_fundamental_data(symbol, cache_hours=24):
    """带缓存的基本面数据获取"""
    
    cache_file = f"cache_{symbol}_fundamental.pkl"
    
    # 检查缓存是否存在且未过期
    if os.path.exists(cache_file):
        file_time = datetime.fromtimestamp(os.path.getmtime(cache_file))
        if datetime.now() - file_time < timedelta(hours=cache_hours):
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
    
    # 获取新数据
    try:
        data = {
            'financial_abstract': ak.stock_financial_abstract(symbol=symbol),
            'balance_sheet': ak.stock_financial_report_sina(
                stock=f"sh{symbol}", symbol="资产负债表"
            ),
            'profit_sheet': ak.stock_financial_report_sina(
                stock=f"sh{symbol}", symbol="利润表"
            )
        }
        
        # 保存到缓存
        with open(cache_file, 'wb') as f:
            pickle.dump(data, f)
        
        return data
        
    except Exception as e:
        print(f"数据获取失败: {e}")
        return {}

# 使用示例
cached_data = cached_fundamental_data("600519")
```

### 3. 批量数据处理

```python
def batch_fundamental_analysis(stock_list):
    """批量基本面数据分析"""
    
    results = {}
    
    for i, stock in enumerate(stock_list):
        try:
            print(f"处理进度: {i+1}/{len(stock_list)} - {stock}")
            
            # 获取基本面数据
            financial_data = ak.stock_financial_abstract(symbol=stock)
            
            # 简单分析
            if not financial_data.empty:
                latest_data = financial_data.iloc[-1]
                results[stock] = {
                    'ROE': latest_data.get('净资产收益率', 'N/A'),
                    'ROA': latest_data.get('总资产报酬率', 'N/A'),
                    'debt_ratio': latest_data.get('资产负债比率', 'N/A')
                }
            else:
                results[stock] = None
            
            # 控制请求频率
            time.sleep(1)
            
        except Exception as e:
            print(f"股票 {stock} 处理失败: {e}")
            results[stock] = None
    
    return results

# 使用示例
stock_list = ["600519", "000858", "002415", "600036", "000002"]
batch_results = batch_fundamental_analysis(stock_list)

# 输出结果
for stock, data in batch_results.items():
    if data:
        print(f"{stock}: ROE={data['ROE']}, ROA={data['ROA']}")
```

## 技术支持和更新

### 最新更新 (2025年9月)
- 新增美股财务数据支持
- 优化港股财务数据格式
- 增强注册制审核数据的实时性
- 修复限售解禁数据的计算问题

### 历史更新
- **2025年3月**: 新增同花顺财务数据接口
- **2024年10月**: 重构新浪财经财务数据模块
- **2024年6月**: 新增注册制审核数据
- **2024年2月**: 增加机构持股分析功能

### 常见问题

1. **财务数据缺失**: 
   - 检查股票代码格式是否正确
   - 确认股票是否已发布财务报告
   - 尝试使用不同数据源的接口

2. **注册制数据更新延迟**:
   - 数据源可能存在更新延迟
   - 建议交叉验证多个数据源

3. **雪球token失效**:
   - 重新获取有效的雪球token
   - 或使用其他数据源替代

4. **港股美股数据格式问题**:
   - 注意不同市场的会计准则差异
   - 数据字段可能与A股不完全一致

---

**模块统计信息**:
- **脚本文件数**: 19个
- **函数接口数**: 51个
- **支持市场**: A股、港股、美股
- **数据类型**: 财务报表、业绩预测、公司治理、新股发行、估值分析
- **主要数据源**: 新浪财经、东方财富、同花顺、雪球等

*最后更新时间: 2025年9月*
*版本状态: 稳定版*
