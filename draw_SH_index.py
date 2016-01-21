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
    print sma
    
    return sma

y= np.array([1,5,3,8,12,6,20,32])
x= np.array(range(0,len(y),1))
sma2= sma(y,2)
sma3= sma(y,3)
'''print x
print type(x)
print y
print type(y)
'''
plt.plot(x,y,"ro",sma2,y,"-", sma3,y,"-")
plt.show()
