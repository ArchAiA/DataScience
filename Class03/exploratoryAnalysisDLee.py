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
drinks.continent == 'EU'
drinks[drinks.continent == 'EU'].country

drinks[drinks.beer_servings >= 158]
drinks[drinks.beer_servings <= 10]
type(drinks[drinks.beer_servings <= 10])
drinks[drinks.beer_servings <= 10][['country', 'beer_servings']] #Again, note the double brackets for printing one column of a dataframe

#Calculate the average 'beer servings' for all of Europe
drinks[drinks.continent == 'EU'][['beer_servings']].mean()
drinks[drinks.continent == 'EU'].beer_servings.mean() #This way is better

#More complex logical filtering
drinks[(drinks.continent == 'EU') & (drinks.wine_servings > 300)]

drinks[(drinks.continent == 'EU') | (drinks.wine_servings > 300)]
drinks[(drinks.continent == 'EU') | (drinks.wine_servings > 300)].beer_servings.mean()

#Show countries that have more than mean beer servings
drinks[drinks.beer_servings > drinks.beer_servings.mean()].country #NOTE dot notation does not work if you have a space in your column name
drinks[drinks.beer_servings > drinks.beer_servings.mean()]['country']




'''EXERCISE #1'''
# 1. What is the maximum number of total literes of pure alcohol
max(drinks.total_litres_of_pure_alcohol)
# Answer: 14.4 - WRONG
#Class answer uses pandas max() not python max()
drinks.total_litres_of_pure_alcohol.max() 



# 2. Which country has the maximum number of total litres of pure alcohol
drinks[drinks.total_litres_of_pure_alcohol == max(drinks.total_litres_of_pure_alcohol)].country
# Answer: Belarus - WRONG
#Class answer uses pandas max() and uses string-list notation
drinks[drinks.total_litres_of_pure_alcohol == drinks.total_litres_of_pure_alcohol.max()]['country']
drinks[drinks.total_litres_of_pure_alcohol == drinks.total_litres_of_pure_alcohol.max()].country



# 3. Does Haiti or Belarus consumre more servings of spirits
drinks[(drinks.country == 'Belarus') | (drinks.country == 'Haiti')][['country', 'spirit_servings']]
# Answer: Belarus



# 4. How many countries have more than 300 wine servings or more than 300 beer
# servings or more than 300 spirit servings?
drinks[(drinks.beer_servings > 300) | (drinks.wine_servings > 300) | (drinks.spirit_servings > 300)].count()
# Answer: 18 - WRONG
#Class answer only counts items in list of matching countries instead of counting all
drinks[(drinks.beer_servings > 300) | (drinks.wine_servings > 300) | (drinks.spirit_servings > 300)].country.count()


# 5. FOr the countries in the previous question, what is the average total
# litres of pure alcohol
drinks[(drinks.beer_servings > 300) | (drinks.wine_servings > 300) | (drinks.spirit_servings > 300)].total_litres_of_pure_alcohol.mean()
# Answer: 10.2611111 - CORRECT
#Class Answer
drinks.total_litres_of_pure_alcohol[(drinks.beer_servings > 300) | (drinks.wine_servings > 300) | (drinks.spirit_servings > 300)].mean()




'''BREAK'''



#SORTING



















