# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:11:22 2015

@author: david
"""

import csv
import sets

with open('chipotle_orders.tsv') as tsv:
    #data = csv.reader(tsv, delimiter = '\t')
    data = [row for row in csv.reader(tsv, delimiter = '\t')]

headers = data[0]
data = data[1:]

orders = set()

for line in data:
    orders.add(line[0])
    
print len(orders)


