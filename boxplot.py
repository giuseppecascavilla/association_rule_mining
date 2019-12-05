# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:28:45 2019

@author: giuseppec
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas
 
df = pandas.read_csv('taxo_surface.csv')


#data.boxplot(column=['question1', 'question2', 'question3']) in order to plot

sns.boxplot( data=df)



# Usual boxplot
ax = sns.boxplot(data=df)
ax = sns.stripplot(data=df, color="orange", jitter=1, size=3.5)
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 6, step=1))
ax.set_xlabel(xlabel='Questions', size=10)
#ax.set_ylabel(ylabel='Y title' , color='b', size=10)
ax.set_ylabel(ylabel='Scale' , size=10)


plt.title("Survey - Taxonomy for Surface Web", size=15, loc="center")


###############################################################################
###############################################################################
###############################################################################
###############################################################################
############## BOX PLOT for DARK Web ##########################################
df2 = pandas.read_csv('taxo_darkweb.csv')

sns.boxplot(data=df2)


# Usual boxplot
ax = sns.boxplot(data=df2)
ax = sns.stripplot(data=df2, color="orange", jitter=1, size=3.5)
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 6, step=1))
ax.set_xlabel(xlabel='Questions', size=10)
#ax.set_ylabel(ylabel='Y title' , color='b', size=10)
ax.set_ylabel(ylabel='Scale' , size=10)

plt.title("Survey - Taxonomy for Deep and Dark Web", size=15, loc="center")