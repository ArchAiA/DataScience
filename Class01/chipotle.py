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
    





tempList = []
tempList = list(orders)
tempList = [int(i) for i in tempList]


tempList.sort()


tempTotal = 0
numberOfOrders = 0



"""THIS IS UNNECESSARILY PROCESSOR INTENSIVE.  ALL WE NEED IS THE TOTAL 
OF ALL OF THE ORDERS / NUMBER OF ORDERS

'''Get the average order total'''
totalOrders = 0
for i in range(len(data)):
    for x in range(len(tempList)):
        if data[i][0] == str(tempList[x]):
            totalOrders += int(data[i][1]) * float(data[i][4][1:])
    #tempTotalOrders += tempOrderTotal
   
print totalOrders / len(tempList)
'''Get the average order total'''
 
THIS IS UNNECESSARILY PROCESSOR INTENSIVE.  ALL WE NEED IS THE TOTAL 
OF ALL OF THE ORDERS / NUMBER OF ORDERS""" 







'''
This is correct: using example of order01 = (a, b) and order02 = (c, d)
the average of the order totals would be 

((a + b) + (c + d)) / 2

Which is the same as 

(a + b + c + d) / 2
''' 

valueOfAllOrders = 0
for index in range(len(data)):
    valueOfAllOrders += int(data[index][1]) * float(data[index][4][1:])

print valueOfAllOrders / len(tempList)










runningTotal = 0
qtyRunningTotal = 0
count = 0
qtyCount = 0
for index in range(len(data)):
    if 'Burrito' in data[index][2]:
        runningTotal += len(data[index][3])
        qtyRunningTotal += len(data[index][3]) * int(data[index][1])
        count += 1
        qtyCount += int(data[index][1]) * 1
print runningTotal
print qtyRunningTotal
print count
print qtyCount

print 'The average number of toppings is %f per burrito' % (float(runningTotal) / float(count))
print 'The average number of toppings is %f when counting duplicate items in an order' % (float(qtyRunningTotal) / float(qtyCount))















uniqueSodas = set()

for index in range(len(data)):
    if ('Canned Soda' or 'Canned Soft Drink') in data[index][2]:
        uniqueSodas.add(data[index][3])
print uniqueSodas















chipOrders = {}


