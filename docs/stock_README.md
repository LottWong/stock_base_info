# AkShare Stock 模块说明文档

## 概述

本文档详细描述了 AkShare 股票（stock）模块下各个脚本文件及其提供的接口功能。该模块主要用于获取股票市场的各类数据，包括实时行情、历史数据、财务信息、资金流向等。

## 目录结构

```
stock/
├── __init__.py                          # 模块初始化文件
├── cons.py                             # 配置常量文件
├── stock_zh_a_sina.py                  # 新浪A股数据
├── stock_zh_kcb_sina.py               # 新浪科创板数据
├── stock_zh_b_sina.py                 # 新浪B股数据
├── stock_hk_sina.py                   # 新浪港股数据
├── stock_us_sina.py                   # 新浪美股数据
├── stock_info.py                      # 股票基本信息
├── stock_fund_em.py                   # 东方财富资金流向
├── stock_board_concept_em.py          # 东方财富概念板块
├── stock_board_industry_em.py         # 东方财富行业板块
├── stock_summary.py                   # 股票市场总貌
└── ... (其他脚本文件)
```

## 主要脚本文件及接口说明

### 1. stock_zh_a_sina.py - 新浪A股数据

**功能描述**: 获取新浪财经A股的实时行情数据和历史行情数据，支持前复权和后复权。

**主要接口**:

#### `stock_zh_a_spot() -> pd.DataFrame`
- **功能**: 获取所有A股的实时行情数据
- **返回**: 包含代码、名称、最新价、涨跌额、涨跌幅等实时行情信息
- **注意**: 重复运行可能被新浪暂时封IP

#### `stock_zh_a_daily(symbol, start_date, end_date, adjust) -> pd.DataFrame`
- **功能**: 获取A股个股的历史行情数据
- **参数**:
  - `symbol`: 股票代码，如 "sh600000"
  - `start_date`: 开始日期，如 "20201103"
  - `end_date`: 结束日期，如 "20201103"
  - `adjust`: 复权类型，可选 "", "qfq", "hfq", "hfq-factor", "qfq-factor"
- **返回**: 历史行情数据，包含开高低收成交量等信息

#### `stock_zh_a_minute(symbol, period, adjust) -> pd.DataFrame`
- **功能**: 获取股票分钟级历史行情数据
- **参数**:
  - `symbol`: 股票代码
  - `period`: 分钟周期，可选 "1", "5", "15", "30", "60"
  - `adjust`: 复权类型
- **返回**: 分钟级行情数据

### 2. stock_info.py - 股票基本信息

**功能描述**: 提供股票的基本信息，包括股票列表、退市信息、名称变更等。

**主要接口**:

#### `stock_info_sz_name_code(symbol) -> pd.DataFrame`
- **功能**: 获取深圳证券交易所股票列表
- **参数**: `symbol` - 可选 "A股列表", "B股列表", "CDR列表", "AB股列表"
- **返回**: 指定类型的股票列表信息

#### `stock_info_sh_name_code(symbol) -> pd.DataFrame`
- **功能**: 获取上海证券交易所股票列表
- **参数**: `symbol` - 可选 "主板A股", "主板B股", "科创板"
- **返回**: 指定类型的股票列表信息

#### `stock_info_bj_name_code() -> pd.DataFrame`
- **功能**: 获取北京证券交易所股票列表
- **返回**: 北交所股票列表信息

#### `stock_info_a_code_name() -> pd.DataFrame`
- **功能**: 获取沪深京A股完整列表
- **返回**: 所有A股的代码和名称

### 3. stock_fund_em.py - 东方财富资金流向

**功能描述**: 获取股票、板块、大盘的资金流向数据。

**主要接口**:

#### `stock_individual_fund_flow(stock, market) -> pd.DataFrame`
- **功能**: 获取个股资金流向数据
- **参数**:
  - `stock`: 股票代码
  - `market`: 市场，可选 "sh", "sz", "bj"
- **返回**: 个股近期资金流数据

#### `stock_individual_fund_flow_rank(indicator) -> pd.DataFrame`
- **功能**: 获取个股资金流向排名
- **参数**: `indicator` - 可选 "今日", "3日", "5日", "10日"
- **返回**: 指定时间段的资金流向排行

#### `stock_market_fund_flow() -> pd.DataFrame`
- **功能**: 获取大盘资金流向数据
- **返回**: 近期大盘的资金流数据

#### `stock_sector_fund_flow_rank(indicator, sector_type) -> pd.DataFrame`
- **功能**: 获取板块资金流向排名
- **参数**:
  - `indicator`: 可选 "今日", "5日", "10日"
  - `sector_type`: 可选 "行业资金流", "概念资金流", "地域资金流"
- **返回**: 指定参数的板块资金流排名数据

### 4. stock_board_concept_em.py - 东方财富概念板块

**功能描述**: 获取概念板块的行情数据和成分股信息。

**主要接口**:

#### `stock_board_concept_name_em() -> pd.DataFrame`
- **功能**: 获取概念板块名称列表
- **返回**: 概念板块基本信息

#### `stock_board_concept_spot_em(symbol) -> pd.DataFrame`
- **功能**: 获取指定概念板块的实时行情
- **参数**: `symbol` - 概念板块名称
- **返回**: 概念板块实时行情数据

#### `stock_board_concept_cons_em(symbol) -> pd.DataFrame`
- **功能**: 获取概念板块的成分股
- **参数**: `symbol` - 概念板块名称
- **返回**: 概念板块成分股列表

### 5. stock_board_industry_em.py - 东方财富行业板块

**功能描述**: 获取行业板块的行情数据和成分股信息。

**主要接口**:

#### `stock_board_industry_name_em() -> pd.DataFrame`
- **功能**: 获取行业板块名称列表
- **返回**: 行业板块基本信息

#### `stock_board_industry_spot_em(symbol) -> pd.DataFrame`
- **功能**: 获取指定行业板块的实时行情
- **参数**: `symbol` - 行业板块名称
- **返回**: 行业板块实时行情数据

#### `stock_board_industry_cons_em(symbol) -> pd.DataFrame`
- **功能**: 获取行业板块的成分股
- **参数**: `symbol` - 行业板块名称
- **返回**: 行业板块成分股列表

### 6. stock_hk_sina.py - 新浪港股数据

**功能描述**: 获取新浪财经港股的实时行情和历史数据。

**主要接口**:

#### `stock_hk_spot() -> pd.DataFrame`
- **功能**: 获取所有港股的实时行情数据
- **返回**: 港股实时行情信息

#### `stock_hk_daily(symbol, adjust) -> pd.DataFrame`
- **功能**: 获取港股个股历史行情数据
- **参数**:
  - `symbol`: 港股代码
  - `adjust`: 复权类型
- **返回**: 港股历史行情数据

### 7. stock_us_sina.py - 新浪美股数据

**功能描述**: 获取新浪财经美股的实时行情和历史数据。

**主要接口**:

#### `get_us_stock_name() -> pd.DataFrame`
- **功能**: 获取美股股票名称和代码
- **返回**: 美股英文名、中文名和代码

#### `stock_us_spot() -> pd.DataFrame`
- **功能**: 获取所有美股的实时数据
- **返回**: 美股实时行情（延迟15分钟）

#### `stock_us_daily(symbol, adjust) -> pd.DataFrame`
- **功能**: 获取美股个股历史数据
- **参数**:
  - `symbol`: 美股代码
  - `adjust`: 复权类型
- **返回**: 美股历史行情数据

### 8. stock_summary.py - 股票市场总貌

**功能描述**: 获取股票市场的整体统计数据和交易概况。

**主要接口**:

#### `stock_szse_summary(date) -> pd.DataFrame`
- **功能**: 获取深交所证券类别统计
- **参数**: `date` - 交易日期
- **返回**: 证券类别统计数据

#### `stock_sse_summary() -> pd.DataFrame`
- **功能**: 获取上交所股票统计数据
- **返回**: 上交所股票统计信息

### 9. 其他重要脚本文件

#### stock_zh_kcb_sina.py - 科创板数据
- `stock_zh_kcb_spot()`: 获取科创板实时行情
- `stock_zh_kcb_daily()`: 获取科创板历史数据

#### stock_zh_b_sina.py - B股数据
- `stock_zh_b_spot()`: 获取B股实时行情
- `stock_zh_b_daily()`: 获取B股历史数据

#### stock_hot_rank_em.py - 热门股票
- `stock_hot_rank_em()`: 获取股票热度排行
- `stock_hot_rank_detail_em()`: 获取热门股票详细信息

#### stock_dzjy_em.py - 大宗交易
- `stock_dzjy_sctj()`: 获取大宗交易市场统计
- `stock_dzjy_mrmx()`: 获取大宗交易明细

#### stock_industry_em.py - 行业数据
- `stock_sector_spot()`: 获取行业板块实时数据
- `stock_sector_detail()`: 获取行业板块详细信息

## 使用示例

```python
import akshare as ak

# 获取A股实时行情
df_spot = ak.stock_zh_a_spot()
print(df_spot.head())

# 获取个股历史数据
df_daily = ak.stock_zh_a_daily(symbol="sh600000", start_date="20220101", end_date="20220131")
print(df_daily.head())

# 获取资金流向数据
df_fund_flow = ak.stock_individual_fund_flow(stock="600094", market="sh")
print(df_fund_flow.head())

# 获取概念板块数据
df_concept = ak.stock_board_concept_name_em()
print(df_concept.head())
```

## 注意事项

1. **频率限制**: 部分接口有访问频率限制，过于频繁调用可能被暂时封IP
2. **数据延迟**: 实时数据可能有15分钟延迟
3. **参数格式**: 注意日期格式和股票代码格式的要求
4. **异常处理**: 建议在使用时添加适当的异常处理机制
5. **数据质量**: 数据来源于第三方网站，可能存在数据缺失或错误的情况

## 更新说明

本模块会根据数据源网站的变化进行定期更新，建议使用最新版本的AkShare库以获得最佳体验。

---

*最后更新时间: 2025年9月*
