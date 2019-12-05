# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:23:56 2019

@author: giuseppec
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori


#df = pd.read_csv(open('Coding_Overview.csv','rU'), encoding='utf-8', engine='c')
#store_data = pd.read_csv('example.csv', header=None)
store_data = pd.read_csv('CLEANED-AssociateRuleMining_dataset.csv', encoding='latin-1')

num_records = len(store_data)
print(num_records)

store_data.head()

records = []
#for i in range(0, 7501): #example range
for i in range(0, num_records): #range of dataset csv
    #records.append([str(store_data.values[i,j]) for j in range(0, 20)]) #example range
    records.append([str(store_data.values[i,j]) for j in range(0, 8)])

### in order to remove NAN value
for i,j in enumerate(records):
    while 'nan' in records[i]: records[i].remove('nan')


association_rules = apriori(records, min_support=0.02, min_confidence=0.8, min_lift=0.5, min_length=1)

association_results = list(association_rules)

print(len(association_results))

print(association_results[0])



"""
#print on screen
for item in association_results:
    # first index of the inner list
    # Contains base item and add item
    pair = item[2][0]
    items = [x for x in pair]
    print(items)
    print("Rule: {} -> {}".format(items[0], items[1]))
#     print("Rule: " + items[0] + " -> {}".format(items[1]))
    #second index of the inner list
    print("Support: " + str(item[1]))
    #third index of the list located at 0th
    #of the third index of the inner list
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
"""


"""
#print on file
"""
file = open('.\output.txt','w') 

for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    #file.write("Rule: " + items[0] + " -> " + items[1] +'\n')
    file.write("Rule: " + str(list(item.ordered_statistics[0].items_base)) + " -> " + str(list(item.ordered_statistics[0].items_add))+'\n')


    #second index of the inner list
    file.write("Support: " + str(item[1]) +'\n')
    
    #third index of the list located at 0th
    #of the third index of the inner list    
    file.write("Confidence: " + str(item[2][0][2]) + '\n')
    file.write("Lift: " + str(item[2][0][3]) + '\n')
    file.write("=====================================\n\n")

file.close()