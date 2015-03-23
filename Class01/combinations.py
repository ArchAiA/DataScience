# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:57:49 2015

@author: david
"""


from itertools import combinations
testList = ['A', 'B', 'C', 'D']
outputList = []

for comb in combinations(testList, 2):
    print comb