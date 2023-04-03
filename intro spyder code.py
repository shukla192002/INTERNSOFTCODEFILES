 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s=pd.read_csv('AAPL Historical Data.csv' ,usecols=[0,1,2,3,4])

pohl_average=s[['Price','Open','High','Low']].mean(axis=1)

obs=np.arange(1,len(s)+1,1)

plt.plot(obs,pohl_average,'r',label='Apple company dataset')
