# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt   

df = pd.read_excel('d:\_stock\SH_1DAY_DATA.xlsx')

df['Date'] = df['Date'].str.slice(0,10)

for i in range(0, len(df['Date'])):
    df['Date'].values[i]= datetime.datetime.strptime(df['Date'].values[i],'%Y-%m-%d')

df.index = df.Date

x=df.Date
y=df.Close



plt.plot(x,y)
plt.show()
