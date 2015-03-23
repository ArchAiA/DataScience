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
sortedOrderList = [int(i) for i in sortedOrderList] #Converts each order number to an int
sortedOrderList.sort() #Sorts the order numbers
"""This takes the orderNumbers set and converts it to a sorted list"""



"""PART 03: Calculate the average price of an order: Calculates the total value of all orders and divides by number of orders"""
dollarValueOfAllOrders = 0
for index in range(len(data)):
    dollarValueOfAllOrders += int(data[index][1]) * float(data[index][4][1:])

print '\n'
print 'The average dollar value for orders was: $%0.2f' % (dollarValueOfAllOrders / len(sortedOrderList))
"""Calculates the total value of all orders and divides by number of orders: PART 03: Calculate the average price of an order"""



"""PART04: Create a list (or set) of all unique sodas and soft drinks that they sell"""
uniqueSodas = set()

for index in range(len(data)):
    if ('Canned Soda' or 'Canned Soft Drink') in data[index][2]:
        uniqueSodas.add(data[index][3])

print '\n'
print "Chiptole stocks the following \'Canned Soft Drinks\' and \'Canned Sodas\':"

for x in uniqueSodas:
    print str(x)
"""PART04: Create a list (or set) of all unique sodas and soft drinks that they sell"""



"""PART05: Calculate the average number of toppings per burrito"""
numberOfBurritoToppings_1 = 0           #Not counting multiples within same order: Method "_1"
numberOfBurritoOrders_1 = 0             #Not counting multiples within same order: Method "_1"
tempToppingsList_1 = []

numberOfBurritoToppings_2 = 0           #Counting multiples within same order: Method "_2"
numberOfBurritoOrders_2 = 0             #Counting multiples within same order: Method "_2"


for index in range(len(data)):
    if 'Burrito' in data[index][2]:
        tempToppingsList_1 = data[index][3].split(',')
        numberOfBurritoToppings_1 += len(tempToppingsList_1)
        numberOfBurritoOrders_1  += 1

        numberOfBurritoToppings_2 += (len(tempToppingsList_1) * int(data[index][1]))
        numberOfBurritoOrders_2 += (1 * int(data[index][1]))

avgNumberOfToppings_1 = float(numberOfBurritoToppings_1) / numberOfBurritoOrders_1
avgNumberOfToppings_2 = float(numberOfBurritoToppings_2) / numberOfBurritoOrders_2


print '\n'
print 'The average number of toppings was %f per burrito' % avgNumberOfToppings_1 #Method "_1"
print 'The average number of toppings was %f when counting duplicate items in orders' % avgNumberOfToppings_2 #Method "_2"
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




for item in chipOrdersList:
    totalChipOrders += int(item[1])
print '_________________________________________'    
print 'The total number of chip orders was: %i ' % totalChipOrders

#This counts the number of chip orders without defaultdict
"""PART 06: Create a dictionary in which the keys represent chip orders and the values represent the total number of orders"""



"""PART 06: Create a dictionary using defaultsdict in which the keys represent chip orders and the values represent the total number of orders"""
from collections import defaultdict

chipInventory = []
chipCount = defaultdict(int)


for line in data:
    if "Chips" in line[2]:
        for i in range(int(line[1])):
            chipInventory.append(line[2])
        
for item in chipInventory:
    chipCount[item] += 1        

print '\n'
print 'Using defaultdict'
print 'The Chip Order Totals By Chip Type Was As Follows:'
print '--------------------------------------------------'
for line in chipCount:
    print line, ': ', chipCount[line]
    
print '_________________________________________'    
print 'The total number of chip orders was:', sum(chipCount.values()) 
"""PART 06: Create a dictionary using defaultsdict in which the keys represent chip orders and the values represent the total number of orders"""



#BONUS: Create a defaultdict that counts the number paired items that were sold
#together in order to find out what customers would like to buy packaged

productsSet = set()
orderItemList = []

#Creating tuples of orderNumbers and orderItems
#Also creating a list of uniqueProducts
for line in data:
    orderItemList.append((line[0], line[2]))
    productsSet.add(line[2])
    
#creating a dictionary where the key is order number
#and the values are order items for that order number
dictionaryOfOrders = defaultdict(list)    
for uniqueNumber, uniqueItem in orderItemList:
    dictionaryOfOrders[uniqueNumber].append(uniqueItem)

#Creating pair-values for each order in dictionaryOfOrders
pairCount = defaultdict(int)
comboList = []
sortList = []

from itertools import combinations
for dictItem in dictionaryOfOrders:

    dictionaryOfOrders[dictItem].sort()
    for comb in combinations(dictionaryOfOrders[dictItem], 2):
        comboList.append(comb)

for item in comboList:
    pairCount[item] += 1        

#Output results
print '\n'
#for pair in pairCount:
#    print pair, ":", pairCount[pair]

for pair in pairCount:
    if pairCount[pair] > 100:
        print pair, ":", pairCount[pair]



#BONUS: Create a defaultdict that counts the number paired items that were sold
#together in order to find out what customers would like to buy packaged









''' INCORRECT BECAUSE IT COUNTS THE NUMBER OF CHARACTERS IN THE BURRITO TOPPINGS LIST ENTRY
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

print '\n'
print 'The average number of toppings is %f per burrito' % (float(numberOfToppingsForCurrentBurrito_1) / float(numberOfBurritoOrders_1)) #Method "_1"
print 'The average number of toppings is %f when counting duplicate items in orders' % (float(numberOfToppingsForCurrentBurrito_2) / float(numberOfBurritoOrders_2)) #Method "_2"

"""PART05: Calculate the average number of toppings per burrito"""
'''





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




