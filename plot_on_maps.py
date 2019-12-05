# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:56:09 2019

@author: giuseppec
"""

import pandas as pd
import os


os.environ['PROJ_LIB'] = r'C:\Users\giuseppec\Anaconda3\Library\share'


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
 
# Set the dimension of the figure
my_dpi=96
plt.figure(figsize=(2600/my_dpi, 1800/my_dpi), dpi=my_dpi)
 
# read the data (on the web)
data = pd.read_csv('maps.csv', sep=";")
 
# Make the background map
m=Basemap(llcrnrlon=-180, llcrnrlat=-65,urcrnrlon=180,urcrnrlat=80)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color="white")
 
# prepare a color for each point depending on the continent.
data['labels_enc'] = pd.factorize(data['homecontinent'])[0]
 
# Add a point per position
m.scatter(data['homelon'], data['homelat'], s=data['n']/3516, alpha=0.4, c=data['labels_enc'], cmap="Set1")
 
# copyright and source data info
plt.text( -170, -58,'Number of attacks around the globe', ha='left', va='bottom', size=9, color='#555555' )
 
# Save as png
plt.savefig('global_attacks.png', bbox_inches='tight')
