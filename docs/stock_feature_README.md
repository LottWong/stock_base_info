# AkShare Stock_Feature 模块说明文档

## 概述

本文档详细描述了 AkShare 股票特色功能（stock_feature）模块下各个脚本文件及其提供的接口功能。该模块是AkShare中功能最丰富、最全面的股票数据模块，包含了**226个函数接口**，涵盖66个脚本文件，提供从基础行情到高级分析的全方位股票数据服务。

## 模块特点

- **功能全面**: 涵盖股票市场的各个方面，从基础数据到高级分析
- **数据源丰富**: 整合东方财富、同花顺、新浪财经、百度股市通等多个权威数据源
- **接口丰富**: 226个函数接口，满足不同层次的数据需求
- **实时性强**: 支持实时行情、资金流向、龙虎榜等实时数据
- **分析深度**: 提供技术分析、财务分析、ESG分析等深度数据

## 模块分类

### 📈 基础行情数据 (Basic Market Data)
- **实时行情**: A股、港股实时价格数据
- **历史数据**: 日线、分钟线历史行情
- **涨跌停**: 涨停板、跌停板数据
- **盘口数据**: 买卖盘、委托数据

### 💰 资金流向分析 (Fund Flow Analysis)
- **个股资金流向**: 主力资金、散户资金流向
- **板块资金流向**: 行业、概念板块资金流向
- **沪深港通**: 北向资金、南向资金流向
- **融资融券**: 融资融券余额、明细数据

### 📊 财务报表数据 (Financial Reports)
- **三大报表**: 资产负债表、利润表、现金流量表
- **业绩预告**: 业绩快报、业绩预告
- **财务指标**: PE、PB、ROE等财务指标
- **分红配股**: 分红送转、配股数据

### 🎯 特色分析功能 (Special Analysis)
- **龙虎榜**: 机构席位、游资动向
- **股东分析**: 股东户数、股东变化
- **技术选股**: 技术指标筛选
- **ESG评级**: 环境、社会、治理评级

### 🔍 市场监控 (Market Monitoring)
- **异动监控**: 大宗交易、异动股票
- **新股数据**: IPO、新股申购
- **停复牌**: 停牌、复牌信息
- **公告数据**: 上市公司公告

## 主要脚本文件分类说明

### 1. 历史行情数据类

#### stock_hist_em.py - 东方财富历史行情
**功能**: 获取股票历史行情数据的核心模块
**接口数量**: 19个函数
**主要功能**:
- `stock_zh_a_spot_em()`: A股实时行情
- `stock_zh_a_hist()`: A股历史日线数据
- `stock_zh_a_hist_min_em()`: A股历史分钟数据
- `stock_hk_spot_em()`: 港股实时行情
- `stock_us_spot_em()`: 美股实时行情

#### stock_hist_tx.py - 腾讯历史行情
**功能**: 腾讯数据源的历史行情
**主要接口**: `stock_zh_a_tick_tx_js()`

### 2. 沪深港通数据类

#### stock_hsgt_em.py - 沪深港通核心数据
**功能**: 沪深港通资金流向和持股数据
**接口数量**: 11个函数
**主要功能**:
- `stock_hsgt_fund_flow_summary_em()`: 沪深港通资金流向汇总
- `stock_hsgt_stock_statistics_em()`: 沪深港通股票统计
- `stock_hsgt_hold_stock_em()`: 沪深港通持股明细
- `stock_hsgt_hist_em()`: 沪深港通历史数据

#### stock_hsgt_exchange_rate.py - 汇率数据
**功能**: 港币汇率相关数据
**接口数量**: 4个函数

#### stock_hsgt_min_em.py - 分钟级数据
**功能**: 沪深港通分钟级资金流向

### 3. 龙虎榜数据类

#### stock_lhb_em.py - 东方财富龙虎榜
**功能**: 龙虎榜数据的核心模块
**接口数量**: 10个函数
**主要功能**:
- `stock_lhb_detail_em()`: 龙虎榜详情
- `stock_lhb_stock_statistic_em()`: 龙虎榜股票统计
- `stock_lhb_jgmx_em()`: 机构明细
- `stock_lhb_yybpm_em()`: 营业部排名

#### stock_lhb_sina.py - 新浪龙虎榜
**功能**: 新浪数据源龙虎榜
**接口数量**: 6个函数

### 4. 涨跌停数据类

#### stock_ztb_em.py - 涨跌停核心数据
**功能**: 涨跌停板数据分析
**接口数量**: 6个函数
**主要功能**:
- `stock_zt_pool_em()`: 涨停股池
- `stock_zt_pool_previous_em()`: 昨日涨停股池
- `stock_zt_pool_strong_em()`: 强势股池
- `stock_zt_pool_sub_new_em()`: 次新股池
- `stock_zt_pool_zbgc_em()`: 炸板股池
- `stock_dt_pool_em()`: 跌停股池

### 5. 财务报表数据类

#### stock_three_report_em.py - 三大财务报表
**功能**: 完整的财务报表数据
**接口数量**: 13个函数
**主要功能**:
- `stock_balance_sheet_by_report_em()`: 资产负债表（按报告期）
- `stock_balance_sheet_by_yearly_em()`: 资产负债表（按年度）
- `stock_profit_sheet_by_report_em()`: 利润表（按报告期）
- `stock_cash_flow_sheet_by_report_em()`: 现金流量表（按报告期）

#### stock_report_em.py - 业绩报告
**功能**: 业绩快报和预告
**接口数量**: 4个函数

### 6. 技术分析类

#### stock_technology_ths.py - 同花顺技术选股
**功能**: 基于技术指标的股票筛选
**接口数量**: 12个函数
**主要功能**:
- `stock_rank_cxg_ths()`: 创新高选股
- `stock_rank_cxd_ths()`: 创新低选股
- `stock_rank_lxsz_ths()`: 连续上涨选股
- `stock_rank_lxxd_ths()`: 连续下跌选股

### 7. 资金流向数据类

#### stock_fund_flow.py - 资金流向分析
**功能**: 个股和板块资金流向
**接口数量**: 5个函数

### 8. 融资融券数据类

#### stock_margin_em.py - 东方财富融资融券
**功能**: 融资融券账户统计

#### stock_margin_sse.py - 上交所融资融券
**功能**: 上交所融资融券数据
**接口数量**: 3个函数

#### stock_margin_szse.py - 深交所融资融券
**功能**: 深交所融资融券数据
**接口数量**: 3个函数

### 9. 股东分析类

#### stock_gdfx_em.py - 股东分析
**功能**: 股东户数、股东变化分析
**接口数量**: 12个函数

#### stock_gdhs.py - 股东户数
**功能**: 股东户数统计
**接口数量**: 2个函数

### 10. 估值分析类

#### stock_a_pe_and_pb.py - PE/PB估值
**功能**: A股PE、PB估值分析
**接口数量**: 4个函数

#### stock_zh_valuation_baidu.py - 百度估值
**功能**: 百度股市通估值数据

#### stock_hk_valuation_baidu.py - 港股估值
**功能**: 港股估值数据

### 11. ESG评级类

#### stock_esg_sina.py - 新浪ESG
**功能**: ESG评级数据
**接口数量**: 5个函数

### 12. 研究报告类

#### stock_research_report_em.py - 研究报告
**功能**: 券商研究报告数据

#### stock_analyst_em.py - 分析师评级
**功能**: 分析师评级和预测
**接口数量**: 2个函数

### 13. 板块概念类

#### stock_board_concept_ths.py - 同花顺概念板块
**功能**: 概念板块数据
**接口数量**: 7个函数

#### stock_board_industry_ths.py - 同花顺行业板块
**功能**: 行业板块数据
**接口数量**: 8个函数

### 14. 特色功能类

#### stock_hot_xq.py - 雪球热门
**功能**: 雪球平台热门股票
**接口数量**: 3个函数

#### stock_inner_trade_xq.py - 内部交易
**功能**: 内部交易数据

#### stock_comment_em.py - 股吧评论
**功能**: 东方财富股吧评论分析
**接口数量**: 6个函数

### 15. 新股数据类

#### stock_yjyg_em.py - 业绩预告
**功能**: 业绩预告数据
**接口数量**: 3个函数

#### stock_yzxdr_em.py - 预增预减
**功能**: 业绩预增预减数据

### 16. 分红配股类

#### stock_fhps_em.py - 东方财富分红配股
**功能**: 分红配股数据
**接口数量**: 2个函数

#### stock_fhps_ths.py - 同花顺分红配股
**功能**: 同花顺分红配股数据

### 17. 大宗交易类

#### stock_qsjy_em.py - 大宗交易
**功能**: 大宗交易数据

### 18. 停复牌数据类

#### stock_tfp_em.py - 停复牌
**功能**: 停复牌信息

### 19. 公告数据类

#### stock_disclosure_cninfo.py - 巨潮资讯公告
**功能**: 上市公司公告数据
**接口数量**: 4个函数

### 20. 其他特色功能

#### stock_cyq_em.py - 筹码分布
**功能**: 筹码分布分析

#### stock_pankou_em.py - 盘口数据
**功能**: 实时盘口数据
**接口数量**: 2个函数

#### stock_value_em.py - 价值分析
**功能**: 股票价值分析

#### stock_buffett_index_lg.py - 巴菲特指数
**功能**: 巴菲特指数计算

## 数据源分布

### 主要数据源统计
- **东方财富 (EM)**: 约60%的接口，提供最全面的数据
- **同花顺 (THS)**: 约15%的接口，专注技术分析
- **新浪财经 (Sina)**: 约10%的接口，提供基础行情
- **巨潮资讯 (CNInfo)**: 约8%的接口，官方公告数据
- **其他数据源**: 约7%的接口，包括雪球、百度等

## 使用示例

### 1. 基础行情数据获取

```python
import akshare as ak

# 获取A股实时行情
df_spot = ak.stock_zh_a_spot_em()
print(df_spot.head())

# 获取历史日线数据
df_hist = ak.stock_zh_a_hist(symbol="000001", 
                            start_date="20240101", 
                            end_date="20240131")
print(df_hist.head())

# 获取分钟线数据
df_min = ak.stock_zh_a_hist_min_em(symbol="000001", 
                                   period="5", 
                                   adjust="qfq")
print(df_min.head())
```

### 2. 涨跌停数据分析

```python
# 获取当日涨停股池
df_zt = ak.stock_zt_pool_em(date="20240301")
print(f"今日涨停股票数量: {len(df_zt)}")

# 获取昨日涨停今日表现
df_zt_prev = ak.stock_zt_pool_previous_em(date="20240301")
print(df_zt_prev.head())

# 获取强势股池
df_strong = ak.stock_zt_pool_strong_em(date="20240301")
print(df_strong.head())
```

### 3. 沪深港通数据

```python
# 沪深港通资金流向汇总
df_hsgt_flow = ak.stock_hsgt_fund_flow_summary_em()
print(df_hsgt_flow.head())

# 沪深港通持股明细
df_hsgt_hold = ak.stock_hsgt_hold_stock_em(symbol="沪股通", 
                                          date="20240301")
print(df_hsgt_hold.head())

# 北向资金历史数据
df_hsgt_hist = ak.stock_hsgt_hist_em(symbol="沪股通")
print(df_hsgt_hist.tail())
```

### 4. 龙虎榜数据

```python
# 龙虎榜详情
df_lhb = ak.stock_lhb_detail_em(start_date="20240301", 
                               end_date="20240301")
print(df_lhb.head())

# 机构席位明细
df_jg = ak.stock_lhb_jgmx_em(start_date="20240301", 
                            end_date="20240301")
print(df_jg.head())

# 营业部排名
df_yyb = ak.stock_lhb_yybpm_em(start_date="20240301", 
                              end_date="20240301")
print(df_yyb.head())
```

### 5. 财务报表数据

```python
# 获取资产负债表
df_balance = ak.stock_balance_sheet_by_report_em(symbol="SH600519")
print(df_balance.head())

# 获取利润表
df_profit = ak.stock_profit_sheet_by_report_em(symbol="SH600519")
print(df_profit.head())

# 获取现金流量表
df_cash = ak.stock_cash_flow_sheet_by_report_em(symbol="SH600519")
print(df_cash.head())
```

### 6. 技术选股

```python
# 创新高选股
df_new_high = ak.stock_rank_cxg_ths(symbol="创月新高")
print(df_new_high.head())

# 连续上涨选股
df_up = ak.stock_rank_lxsz_ths(symbol="连续3日上涨")
print(df_up.head())

# 放量上涨选股
df_volume_up = ak.stock_rank_flsz_ths(symbol="放量上涨")
print(df_volume_up.head())
```

### 7. 资金流向分析

```python
# 个股资金流向
df_fund_individual = ak.stock_individual_fund_flow(stock="600519", 
                                                  market="sh")
print(df_fund_individual.head())

# 板块资金流向排名
df_sector_flow = ak.stock_sector_fund_flow_rank(indicator="今日", 
                                               sector_type="行业资金流")
print(df_sector_flow.head())
```

### 8. 融资融券数据

```python
# 融资融券账户统计
df_margin_account = ak.stock_margin_account_info()
print(df_margin_account.head())

# 上交所融资融券明细
df_margin_sse = ak.stock_margin_sse(trade_date="20240301")
print(df_margin_sse.head())
```

### 9. ESG评级数据

```python
# ESG评级数据
df_esg = ak.stock_esg_rate_sina()
print(df_esg.head())

# ESG评级详情
df_esg_detail = ak.stock_esg_hz_sina()
print(df_esg_detail.head())
```

### 10. 批量数据获取示例

```python
import akshare as ak
import pandas as pd

def get_comprehensive_stock_data(symbol="000001", date="20240301"):
    """获取股票的综合数据"""
    data_dict = {}
    
    # 基础行情
    try:
        data_dict['历史行情'] = ak.stock_zh_a_hist(symbol=symbol)
    except:
        data_dict['历史行情'] = pd.DataFrame()
    
    # 资金流向
    try:
        data_dict['资金流向'] = ak.stock_individual_fund_flow(stock=symbol, market="sz")
    except:
        data_dict['资金流向'] = pd.DataFrame()
    
    # 龙虎榜
    try:
        data_dict['龙虎榜'] = ak.stock_lhb_detail_em(start_date=date, end_date=date)
        data_dict['龙虎榜'] = data_dict['龙虎榜'][data_dict['龙虎榜']['代码'] == symbol]
    except:
        data_dict['龙虎榜'] = pd.DataFrame()
    
    # 涨停分析
    try:
        zt_pool = ak.stock_zt_pool_em(date=date)
        data_dict['涨停情况'] = zt_pool[zt_pool['代码'] == symbol]
    except:
        data_dict['涨停情况'] = pd.DataFrame()
    
    return data_dict

# 使用示例
stock_data = get_comprehensive_stock_data("000001", "20240301")
for key, df in stock_data.items():
    print(f"{key}: {len(df)} 条记录")
```

## 高级应用场景

### 1. 量化选股策略

```python
def quantitative_stock_selection():
    """基于多维度数据的量化选股"""
    
    # 获取涨停股池
    zt_stocks = ak.stock_zt_pool_em()
    
    # 获取技术面强势股
    strong_stocks = ak.stock_zt_pool_strong_em()
    
    # 获取资金流向排名
    fund_flow_rank = ak.stock_individual_fund_flow_rank(indicator="5日")
    
    # 获取龙虎榜活跃股
    lhb_stocks = ak.stock_lhb_detail_em(
        start_date="20240301", 
        end_date="20240301"
    )
    
    # 综合分析选股逻辑
    selected_stocks = []
    
    return selected_stocks
```

### 2. 市场情绪分析

```python
def market_sentiment_analysis():
    """市场情绪综合分析"""
    
    # 涨跌停统计
    zt_count = len(ak.stock_zt_pool_em())
    dt_count = len(ak.stock_dt_pool_em())
    
    # 沪深港通资金流向
    hsgt_flow = ak.stock_hsgt_fund_flow_summary_em()
    
    # 融资融券情况
    margin_info = ak.stock_margin_account_info()
    
    # 龙虎榜活跃度
    lhb_activity = ak.stock_lhb_detail_em(
        start_date="20240301", 
        end_date="20240301"
    )
    
    sentiment_score = calculate_sentiment_score(
        zt_count, dt_count, hsgt_flow, margin_info, lhb_activity
    )
    
    return sentiment_score
```

### 3. 风险监控系统

```python
def risk_monitoring_system():
    """股票风险监控系统"""
    
    # 异动股票监控
    abnormal_stocks = ak.stock_zt_pool_zbgc_em()  # 炸板股
    
    # 大宗交易监控
    block_trades = ak.stock_qsjy_em()
    
    # 停复牌监控
    suspended_stocks = ak.stock_tfp_em()
    
    # 融资融券风险
    margin_risk = ak.stock_margin_account_info()
    
    risk_report = {
        '异动股票': len(abnormal_stocks),
        '大宗交易': len(block_trades),
        '停牌股票': len(suspended_stocks),
        '融资融券风险': analyze_margin_risk(margin_risk)
    }
    
    return risk_report
```

## 数据质量和注意事项

### 1. 数据时效性
- **实时数据**: 延迟通常在15分钟以内
- **历史数据**: 通常T+1更新
- **财务数据**: 季报发布后1-2个工作日更新
- **公告数据**: 实时更新

### 2. 数据完整性
- **A股数据**: 覆盖沪深京三个交易所
- **港股数据**: 覆盖港股通标的
- **历史数据**: 部分接口可追溯到2005年
- **财务数据**: 覆盖2007年以来的完整数据

### 3. 使用限制
- **频率控制**: 建议单个接口调用间隔不少于1秒
- **并发限制**: 建议同时调用接口不超过5个
- **数据量限制**: 单次获取数据量建议不超过10000条
- **IP限制**: 过于频繁调用可能被暂时封IP

### 4. 错误处理
```python
import akshare as ak
import time

def safe_data_fetch(func, *args, **kwargs):
    """安全的数据获取函数"""
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            result = func(*args, **kwargs)
            if not result.empty:
                return result
            else:
                print(f"获取到空数据，第{attempt+1}次重试...")
        except Exception as e:
            print(f"数据获取失败: {e}，第{attempt+1}次重试...")
        
        if attempt < max_retries - 1:
            time.sleep(retry_delay)
    
    print(f"经过{max_retries}次重试仍然失败")
    return pd.DataFrame()

# 使用示例
df = safe_data_fetch(ak.stock_zh_a_spot_em)
```

## 性能优化建议

### 1. 数据缓存策略
```python
import pickle
import os
from datetime import datetime, timedelta

def cached_data_fetch(func, cache_file, cache_hours=1, *args, **kwargs):
    """带缓存的数据获取"""
    if os.path.exists(cache_file):
        file_time = datetime.fromtimestamp(os.path.getmtime(cache_file))
        if datetime.now() - file_time < timedelta(hours=cache_hours):
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
    
    # 获取新数据
    data = func(*args, **kwargs)
    
    # 保存到缓存
    with open(cache_file, 'wb') as f:
        pickle.dump(data, f)
    
    return data
```

### 2. 批量数据处理
```python
def batch_stock_analysis(stock_list, date="20240301"):
    """批量股票分析"""
    results = {}
    
    # 批量获取基础数据
    all_spot_data = ak.stock_zh_a_spot_em()
    
    for stock in stock_list:
        try:
            # 从已获取的数据中筛选
            stock_spot = all_spot_data[all_spot_data['代码'] == stock]
            
            # 获取个股特有数据
            stock_flow = ak.stock_individual_fund_flow(stock=stock, market="sz")
            
            results[stock] = {
                'spot': stock_spot,
                'fund_flow': stock_flow
            }
            
            # 控制请求频率
            time.sleep(0.5)
            
        except Exception as e:
            print(f"股票 {stock} 数据获取失败: {e}")
            results[stock] = None
    
    return results
```

## 更新日志

### 最新更新 (2025年9月)
- 新增异动股票监控功能
- 优化沪深港通数据获取速度
- 增强财务数据的完整性
- 修复部分接口的数据格式问题

### 历史更新
- **2024年11月**: 新增涨停板行情专题
- **2024年9月**: 增加技术选股功能
- **2024年6月**: 优化融资融券数据接口
- **2024年4月**: 重构龙虎榜数据模块

## 技术支持

### 常见问题
1. **数据获取失败**: 检查网络连接，确认股票代码格式
2. **数据格式异常**: 更新到最新版本的AkShare
3. **访问频率限制**: 增加请求间隔时间
4. **内存占用过高**: 分批获取数据，及时清理无用变量

### 反馈渠道
- GitHub Issues: 提交bug报告和功能请求
- 官方文档: 查看最新的接口文档
- 社区讨论: 参与技术讨论和经验分享

---

**模块统计信息**:
- **脚本文件数**: 66个
- **函数接口数**: 226个
- **数据源数**: 10+个
- **覆盖市场**: A股、港股、美股
- **数据类型**: 实时行情、历史数据、财务报表、资金流向、技术指标等

*最后更新时间: 2025年9月*
*版本状态: 稳定版*
