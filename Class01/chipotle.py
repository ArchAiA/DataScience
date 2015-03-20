# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:11:22 2015

@author: david
"""

import csv

print '\n'




"""PART 01: Read in the data, parse it, and store it in a list of lists called 'data'"""
with open('chipotle_orders.tsv') as data:
    #data = csv.reader(tsv, delimiter = '\t')
    data = [row for row in csv.reader(data, delimiter = '\t')]
"""PART 01: Read in the data, parse it, and store it in a list of lists called 'data'"""

"""PART 02: Separate the header and data into two different lists"""
headers = data[0] #header row drawn from first entry in data
data = data[1:] #data is a slice of the remaining information
"""PART 02: Separate the header and data into two different lists"""



"""This gets a set of orders.  Each order number is unique"""
orderNumbers = set()

for line in data:
    orderNumbers.add(line[0])
"""This gets a set of orders.  Each order number is unique"""



"""This takes the orderNumbers set and converts it to a sorted list"""
sortedOrderList = []
sortedOrderList = list(orderNumbers)
sortedOrderList = [int(i) for i in tempList] #Converts each order number to an int
sortedOrderList.sort() #Sorts the order numbers
"""This takes the orderNumbers set and converts it to a sorted list"""



"""PART 03: Calculate the average price of an order: Calculates the total value of all orders and divides by number of orders"""
dollarValueOfAllOrders = 0
for index in range(len(data)):
    dollarValueOfAllOrders += int(data[index][1]) * float(data[index][4][1:])

print 'The average dollar value for orders is: $%0.2f' % (dollarValueOfAllOrders / len(sortedOrderList))
print '\n'
"""Calculates the total value of all orders and divides by number of orders: PART 03: Calculate the average price of an order"""



"""PART04: Create a list (or set) of all unique sodas and soft drinks that they sell"""
uniqueSodas = set()

for index in range(len(data)):
    if ('Canned Soda' or 'Canned Soft Drink') in data[index][2]:
        uniqueSodas.add(data[index][3])
        
print "Chiptole stocks the following \'Canned Soft Drinks\' and \'Canned Sodas\':"

for x in uniqueSodas:
    print str(x)
"""PART04: Create a list (or set) of all unique sodas and soft drinks that they sell"""



"""PART05: Calculate the average number of toppings per burrito"""
numberOfToppingsForCurrentBurrito_1 = 0 #Not counting multiples within same order: Method "_1"
numberOfBurritoOrders_1 = 0             #Not counting multiples within same order: Method "_1"

numberOfToppingsForCurrentBurrito_2 = 0 #Counting multiples within same order: Method "_2"
numberOfBurritoOrders_2 = 0             #Counting multiples within same order: Method "_2"

for index in range(len(data)):
    if 'Burrito' in data[index][2]:
        numberOfToppingsForCurrentBurrito_1 += len(data[index][3]) #Method "_1"
        numberOfToppingsForCurrentBurrito_2 += len(data[index][3]) * int(data[index][1]) #Method "_2"
        numberOfBurritoOrders_1 += 1 #Method "_1"
        numberOfBurritoOrders_2 += int(data[index][1]) * 1 #Method "_2"
print 'The average number of toppings is %f per burrito' % (float(numberOfToppingsForCurrentBurrito_1) / float(numberOfBurritoOrders_1)) #Method "_1"
print 'The average number of toppings is %f when counting duplicate items in orders' % (float(numberOfToppingsForCurrentBurrito_2) / float(numberOfBurritoOrders_2)) #Method "_2"
print '\n'
"""PART05: Calculate the average number of toppings per burrito"""







"""PART 06: Create a dictionary in which the keys represent chip orders and the values represent the total number of orders"""
chipOrdersDict = {}
chipOrdersSet = set()
chipOrdersList = []
totalChipOrders = 0



print '\n'
print "The Chip Order Totals By Chip Type Was as Follows:"
print "--------------------------------------------------" 

#This counts the number of chip orders without defaultdict

#This creates a list of tuples.  Each tuple contains item name, and qty
#It also creates a set of the unique values of item names
for line in data:
    if 'Chips' in line[2]:     #Gets every line of data that has Chips in the item name
        tempTuple = ([line[2], int(line[1])])    #Creates a tuple if Chips is found in the item name
        chipOrdersList.append(tempTuple)      #Appends the tuple to a chipOrders_2 list
        chipOrdersSet.add(line[2])          #Independently creates a set with each chip order type
        
for item in chipOrdersSet:
    chipOrdersDict[item] = int(0)        

for item in chipOrdersList:
    chipOrdersDict[item[0]] += item[1]        

for key, value in chipOrdersDict.iteritems():
    print key, ": ", value    
 #This creates a list of tuples.  Each tuple contains item name, and qty
#It also creates a set of the unique values of item names




for item in chipOrders_2:
    totalChipOrders += int(item[1])
print '\n'
print 'The total number of chip orders was: %i ' % totalChipOrders
#This counts the number of chip orders without defaultdict
"""PART 06: Create a dictionary in which the keys represent chip orders and the values represent the total number of orders"""



















""" LAME ASS AVERAGE ORDER CALCULATION
THIS IS UNNECESSARILY PROCESSOR INTENSIVE.  
ALL WE NEED IS THE (TOTAL OF ALL OF THE ORDERS / NUMBER OF ORDERS)
THIS ITERATES THROUGH EACH OBJECT IN DATA AND THEN ITERATES THROUGH THE
LIST OF UNIQUE ORDERS AND COMPARES THE TWO DATAPOINTS
MOST OF THE PROCESSOR CYCLES ARE WASTED BECAUSE THE NON MATCHES FAR
OUTNUMBER THE MATCHES

'''Get the average order total'''

tempTotal = 0
numberOfOrders = 0

totalOrders = 0
for i in range(len(data)):
    for x in range(len(sortedOrderList)):
        if data[i][0] == str(sortedOrderList[x]):
            totalOrders += int(data[i][1]) * float(data[i][4][1:])
    #tempTotalOrders += tempOrderTotal
   
print totalOrders / len(sortedOrderList)
'''Get the average order total'''
 
THIS IS UNNECESSARILY PROCESSOR INTENSIVE.  ALL WE NEED IS THE TOTAL 
OF ALL OF THE ORDERS / NUMBER OF ORDERS

The correct way is above is correct: using example of 
order01 = (a, b) and order02 = (c, d)
the average of the order totals would be 
((a + b) + (c + d)) / 2
Which is the same as 
(a + b + c + d) / 2
LAME ASS AVERAGE ORDER CALCULATION """





