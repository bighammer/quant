# -*- coding: utf-8 -*-
"""
Purpose
    Learn how to process data with python and plot

"""

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#
# Constant definition
#

# Initial capital is 1,000,000
# Equity = stocks + cash


#

df = pd.read_excel('.\SH_1DAY_DATA.xlsx')

df['Date'] = df['Date'].str.slice(0,10)

for i in range(0, len(df['Date'])):
    df['Date'].values[i]= datetime.datetime.strptime(df['Date'].values[i],'%Y-%m-%d')

# df.index = df.Date

# x=df.Date
# y=df.Close

# Moving average
def sma(x, n):
    """
    compute an n period simple moving average.

    """
    sma = pd.rolling_mean(x,n)
    # print sma

    return sma


# Strategy 01
#   simple moving average stragety
#

# Performance metrics review

#
#y= np.array([1,5,3,8,12,6,20,32])
#x= np.array(range(0,len(y),1))
#sma2= sma(y,2)
#sma3= sma(y,3)
'''print x
print type(x)
print y
print type(y)
'''
#plt.plot(x,y,"ro",sma2,y,"-", sma3,y,"-")
#plt.show()

"""
    Moving Average Rules
        o Variation 1
           Buy when close crosses above x day moving average
           Sell when close crosses below x day moving average
        o Variation 2
           Buy when x day moving average crosses above y day moving average
           Sell when x day moving average crosses below y day moving average
"""

# Variation 1: Single MA
def ts_single_ma( window, data ):

    return

days=60
df['SMA'+str(days)]=sma(df['Close'],days)
df['Singnal'] = np.zeros(len(df['Close']))
buys=[]
sells=[]
trades=[]

for i in range(0, len(df['Date'])):
    if df['Close'][i] > df['SMA'+str(days)][i]:
        #df['Singnal'][i] = 1;
        #print 'B';
        buys.append([df.Date[i], df.Close[i]])
        #trades.append(['buy_open', df.Date[i]],df.Close[i])
    if df['Close'][i] <= df['SMA'+str(days)][i]:
        #df['Singnal'][i] = -1;
        #print 'S';
        sells.append([df.Date[i], df.Close[i]])
#print buys

"""
    Channel Breakout Rules
       Buy if today’s close is the highest close of the past x days
       Sell if today’s close is the lowest close of the past x days
"""
# Prepare the data
# - create two new columes:  sma_M, sma_N
# - sma is based on *close* price

"""
    Performance Matrics
    Equity
    o Net Profit
    o Average Profit / trade
    o Wins/Losses
    o Profit Factor
    o Max Drawdown
    o Sharp Ratio
    o K-Ratio

    o # of Trades
    o Win Ratio
    o Avarage Win
    o Avarage Loss
"""

#plt.plot(x,y,"ro",sma2,y,"-", sma3,y,"-")
#plt.show()
