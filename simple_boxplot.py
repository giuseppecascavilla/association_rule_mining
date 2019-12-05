# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:26:11 2019

@author: giuseppec
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
 
# Dataset: Surface WEB
q1 = [4,4,3,3,4,3,2,3,2,3,4,3,2,1,4]
q2 = [5,5,4,4,4,4,3,5,3,4,4,3,4,4,3]
q3 = [4,5,5,4,5,5,3,4,3,5,4,3,4,4,3]
q4 = [5,5,5,4,5,5,4,5,4,5,4,3,3,4,4]
q5 = [4,4,3,5,3,5,4,5,4,4,3,3,4,4,5]
q6 = [5,4,3,5,4,5,4,5,4,2,3,3,5,3,4]
q7 = [3,2,4,3,3,5,5,2,5,5,4,3,5,4,5]
q8 = [4,4,3,4,4,5,4,3,4,4,3,3,2,1,3]
q9  = [5,2,3,5,4,5,5,5,5,3,3,3,4,5,3]
q10 = [4,5,4,5,5,4,5,4,5,5,3,3,4,2,4]
q11 = [5,5,5,3,4,4,5,5,5,4,3,3,3,3,4]
q12 = [4,3,5,4,5,4,5,4,5,5,3,3,3,3,5]

# Dataset: Dark WEB

qd1 = [4,5,4,4,4,3,4,3,4,3,3,3,3,2,3]
qd2 = [3,4,4,5,3,4,4,3,4,4,3,3,2,2,3]
qd3 = [3,3,4,5,4,4,4,4,4,5,4,3,4,3,4]
qd4 = [4,4,5,3,4,5,4,5,4,3,4,3,3,3,4]
qd5 = [3,5,5,4,5,3,5,5,5,5,4,3,3,3,5]


box_plot_data=[q1,q2,q3,q4]

#plt.boxplot(box_plot_data)
plt.boxplot(box_plot_data,patch_artist=True,labels=['question1','question2','question3','question4'])


plt.show()