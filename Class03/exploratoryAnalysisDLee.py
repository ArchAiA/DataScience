# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:50:34 2015

@author: david
"""

#Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


'''Reading Files, Summarizing, Selecting, Filtering, Sorting'''
drinks = pd.read_table('drinks.csv', sep=',') #For reading from any file
drinks = pd.read_csv('drinks.csv') #read_csv automatically sets sep to ','

#For reading from URLs
#drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/drinks.csv')
'''Reading Files, Summarizing, Selecting, Filtering, Sorting'''

drinks
type(drinks)
drinks.head()
drinks.head(10)
drinks.tail()
drinks.describe() #CAUTION: default is to take the first row as column names
#print drinks.describe(include='all')
drinks.index
drinks.columns
drinks.dtypes
'The number of rows is', drinks.shape[0], 'and the number of columns is,', drinks.shape[1]
drinks.shape

drinks.values #If you want the numpy array back, you can use values() and this will return the numpy array
drinks.info()

#Two ways of specifying return data in a dataframe
drinks.beer_servings #Addressing as an attribute
drinks['beer_servings'] #Addressing as a dictionary

#Sometimes it is important to know the type because some operations can 
#only be performed on dataframes while some can only be performed on series
type(drinks.beer_servings) 


#Printing two columns
drinks[['beer_servings', 'wine_servings']]#Basic form for printing columns from a dataframe
cols = ['beer_servings', 'wine_servings'] #You can also store what you want to extract in a list
drinks[cols]                              #And then pass that list to the pandas object (dataframe)  


#Calculate the average 'beer_servings' for the entire dataset
drinks.describe() #Gives us summary stats for the entire dataframe
drinks.beer_servings.describe() #Gives us summary stats for the specified element
drinks.beer_servings.mean() #Gives us the specific summary stat that we are looking for
drinks.beer_servings.max()
drinks.beer_servings.min()
drinks.beer_servings.count()
drinks.beer_servings.sum()

float(drinks.beer_servings.sum()) / drinks.beer_servings.count() #Calculating the mean beer_servings globally the long way



#Count the number of occurrences of each 'continent' value
drinks.continent.value_counts()







