# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:03:39 2015

@author: david
"""
import collections

#Counter counts the objects passed as arguments, and places them in a dict
a = collections.Counter('gallahad')
b = collections.Counter({'red': 4, 'blue': 2})
c = collections.Counter(cats = 4, dogs = 8)


#The long way around...
print a.keys()[0], ":", a[a.keys()[0]]
print a.keys()[1], ":", a[a.keys()[1]]
print a.keys()[2], ":", a[a.keys()[2]]
print a.keys()[3], ":", a[a.keys()[3]]
print a.keys()[4], ":", a[a.keys()[4]]
print '\n'

#Using iteritems
for key, value in a.iteritems():
    print key, ">", value
print '\n'
    
#Elements will return each element in the Counter object as many times as they are counted
print list(a.elements())
print '\n'

# most_common([n]) will return the n most common elements
print a.most_common(2)
print '\n'

#Look into: Counter(dict(list_of_pairs)) which converts a list of (elem, cnt) pairs

#Deques are fast lists that are good for push/pop off of stacks


#DEFAULTDICT
#defaultdict takes the first thing being iterated through and makes it a key
#The value is then determined according to how the defaultdict variable was declared
#If it was c = defaultdict(int) the value will start at zero
#If it was d = defaultdict(list) the value will start as an empty list

from collections import defaultdict

#FOR LISTS
testList = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
listDict = defaultdict(list) #Indicates that the values in the dict will be lists
for k, v in testList:
    listDict[k].append(v) #Because the values in this dict are lists, we must use append

print listDict.items()
print '\n'


#FOR INT
#When a defaultdict(int) is declared, the dict can be used as a counter
testString = 'Mississippi'
intDict = defaultdict(int)

for k in testString:
    intDict[k] += 1

print intDict.items()
print 's shows up', intDict['s'], 'times'
print '\n'

#Other constant functions
#If you would like to use something besides 0 as the default return
#you can use itertools.repeat()
import itertools

def constant_factory(value):
    return itertools.repeat(value).next
    
factoryDict = defaultdict(constant_factory('<missing>'))
factoryDict.update(name = 'John', action = 'ran')
print '%(name)s %(action)s to %(object)s' % factoryDict
print '\n'

#SETS
#using defaultdict(set) makes the defaultdic useful for bulding dicts of sets
setTest = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
setDict = defaultdict(set)

for k, v in setTest:
    setDict[k].add(v)
    
print setDict.items()