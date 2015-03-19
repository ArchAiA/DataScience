# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:11:22 2015

@author: david
"""

import csv
with open('chipotle_orders.tsv') as tsv:
    data = csv.reader(tsv, delimiter = '\t')
    print line[3]
            
