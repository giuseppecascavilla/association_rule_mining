# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:55:12 2019

@author: giuseppec
"""

import matplotlib.pyplot as plt

# Data to plot
labels = 'Individuals affected \n in Dark Web', 'Individuals affected \n in Surface Web'
sizes = [1484569785, 3652268106]
colors = ['yellowgreen', 'lightskyblue']
explode = (0, 0,)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
#plt.show()
plt.title("Individuals Affected from the Attacks ", size=15, loc="center")
