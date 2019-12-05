# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:08:31 2019

@author: giuseppec
"""


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas
 
df = pandas.read_csv('data_retrieved.csv')
df.head()



#plt.xticks(np.arange(0, 1, step=0.2))

ax = df.plot.barh(y='%', x='User Attribute', rot=0)