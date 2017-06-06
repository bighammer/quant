

# Howto
How to deal with proxy (access internet data via proxy)

## Windows command window( cmd ) setup

set HTTPS_PROXY=http://username:passwd@proxy.huawei.com:8080

set HTTP_PROXY=http://username:passwd@proxy.huawei.com:8080

## git setup

git config -l # check the current value of configuration

git config --global http.proxy=http://usr:passwd@proxy.huawei.com:8080

git config --global http.proxy=http://usr:passwd@proxy.huawei.com:8080

git config --global http.sslverify=false

# Finance statistics with Python
## Basics
* How to prepare data to be processed ?
  - **Note: data needs to be with source file.**
  - dynamic draw: It seems matplotlib is OK to draw dynamically.


* How to analyze a trading system's performance ?
  - Start with a simple one: MA
*

## Plans
* candle sticks
  - Do I need to create a candle stick class ? or make use of matplotlib.Finance
  -


# Finance Terms
=======
# Terms
** Note: The description is not from dictionary. Most of them is based on my personal understanding **   

|Terms  | 中文   |Description |
|:------|:-------|:----------|
|Equity |净值|The total value of Cash + Stocks + Commodities|
|Index  |指数|A set of stocks with which to indicate the market trend|  
|symbols|股票代码|Stock or Commodity ID, it could also mean some index such as CPI,etc.|
|Commodity|商品|Items of future markets, such as Gold, Oil, Wheat, etc.|  
|Market |市场|Defferent stock, Commodity markets|
|Profit |利润|Revenue minus cost. The amount one makes on a transaction.|
|Security|证券|General name of any stock or future or others|
|Drawdown|回撤|Drawdown from the peak|
