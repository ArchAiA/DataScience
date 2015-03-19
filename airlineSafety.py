# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:32:34 2015

@author: david
"""

'''
#FIRST WAY OF OPENING FILE
f = open('airline_safety.csv', 'rU')

something = f.read()
f.close()
#FIRST WAY OF OPENING FILE
'''

'''
#CONTEXT MANAGER WAY OF OPENING A FILE - AUTO CLOSE FILE
with open('airline_safety.csv', 'RU') as f:
    f.read()
#CONTEXT MANAGER WAY OF OPENING A FILE - AUTO CLOSE FILE
'''

'''
#Read the whole file at once, return a list of lines
with open('airline_safety.csv', 'rU') as f:
    something = f.readlines()
#Read the whole file at once, return a list of lines
'''


'''
#Using a list comprehension to dulplicate readiness
#When you iterate through a file, the iteration is by line

with open('airline_safety.csv', 'rU') as f:
    something = [row for row in f]


#Using a list comprehension to dulplicate readiness
'''







#CLASS EXERCISE

#Using the csv module to create a list of lists
#This takes the csv file, and creates a list of lists delimiting the inside lists at \n
import csv
with open('airline_safety.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]
    
header = data[0]
data = data[1:]


#EXERCISE:
# 1) Create a list of airline names without the star
# 2) Create a list of the same length as the original list that contains 1 if 
# there is a start, and a 0 if not


noStars = []
stars = []
for line in data:
    #print line[0]
    include = line[0].find('*')

    if include == -1:
        noStars.append(line[0])
    else:
        stars.append(line[0])
    #noStars.append()


airlines = []
starred = []
for row in data:
    if row[0][-1] == '*':
        starred.append(1)
        airlines.append(row[0][:-1])
    else:
        starred.append(0)
        airlines.append(row[0])
        
        
    



