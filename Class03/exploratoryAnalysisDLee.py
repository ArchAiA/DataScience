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
drinks.beer_servings.order() #only works for a series
drinks.spirit_servings.order()
drinks.sort_index() #This automatically sorts by the primary index
drinks.sort_index(by='beer_servings') #This sorts by a specific column
drinks.sort_index(by='beer_servings').head(10)
drinks.sort_index(by='beer_servings', ascending=False).head(10)
drinks.sort_index(by=['beer_servings', 'wine_servings'], ascending = False).head(10) #Adding a secondary sort column


#Determine which 10 countries have the highest 'total_litres_of_pure_alcohol'
drinks.sort_index(by='total_litres_of_pure_alcohol', ascending=False).head(10)
drinks.sort_index(by='total_litres_of_pure_alcohol').tail(10)


# Determine which country has the highest value for beer servings
drinks.sort_index(by='beer_servings', ascending=False).head(1)
drinks.sort_index(by='beer_servings').tail(1)
drinks[drinks.beer_servings == drinks.beer_servings.max()].country
drinks[drinks.beer_servings == drinks.beer_servings.max()]['country']


#Use dot notation to string together commands
#How many countries in each continent have beer_servings greater than 182?

drinks[drinks.beer_servings > 182].continent.value_counts()




#Add a new column as a function of existing columns
#NOTE: Can't assign to an attribute (e.g., 'drinks.total_servings') - THIS MEANS DOT NOTATION WILL NOT WORK IN ASSIGNMENT WHEN THE ATTRIBUTE DOES NOT ALREADY EXIST
#Using brackets resembles adding a new dictionary key/value pair
drinks['total_servings'] = drinks.beer_servings + drinks.wine_servings + drinks.spirit_servings
drinks['alcohol_ml'] = drinks.total_litres_of_pure_alcohol * 1000
drinks.total_servings #What about NOTE - NOTE WAS ONLY ADDRESSSING INITIAL ASSIGNMENT
drinks.alcohol_ml #What about NOTE - NOTE WAS ONLY ADDRESSSING INITIAL ASSIGNMENT
drinks.tail(10)




'''Split Apply Combine'''

#For each continent, caluclate mean beer servings
drinks.groupby('continent').beer_servings.mean()

#For each continent, calculate the mean of all of the numberic columns
drinks.groupby('continent').mean()
#Can I use groupby with logical operands (etc. beer_servings > 180)?

drinks.groupby(['continent', 'country']).beer_servings.mean()
drinks.groupby([drinks.beer_servings < 50, drinks.beer_servings >= 50]).count() #???
drinks.groupby([drinks.beer_servings < 50, drinks.beer_servings >= 50]).mean() #???


#For each continent count number of occurrences
drinks.groupby('continent').continent.count() #Returns a list of number of requested item in the group 
drinks.groupby('continent').count() #Returns a list of each column total for each continent
drinks.continent.value_counts() #I think that this would be faster than the above




'''A little numpy'''
probs = np.array([0.51, 0.50, 0.02, 0.49, 0.78])
#np.where functions like an IF statement in excel
# np.where(condition, value if true, value if false)
np.where(probs >= 0.5, 1, 0) #Returns a 1 for the element if greater than 0.5, a zero if otherwise
drinks['lots_of_beer'] = np.where(drinks.beer_servings > 300, 1, 0) #Will create a new column with lots_of_beer true if > 300 beer units are consumed
drinks.sort_index(by='lots_of_beer').tail(15)

drinks['full_of_drunkards'] = np.where(drinks.total_litres_of_pure_alcohol > 10, 'Drunks', 'Not So Drunks')
drinks.sort_index(by="total_litres_of_pure_alcohol").tail(10)




'''EXERCISE 2'''
#What is the average number of total litres of pure alcohol for each continent?
drinks.groupby('continent').total_litres_of_pure_alcohol.mean()
#CORRECT



#For each continent, calculate the mean wine_servings for all countries who 
#have a spirit servings greater than the overall spirit servings mean
drinks[drinks.spirit_servings > drinks.spirit_servings.mean()].groupby('continent').wine_servings.mean()
#CORRECT



#Per continent, for all of the countries that drink more beer servings than
#the average number of beer servings, what is the average number of wine servings?

#TWO ATTEMPTS.  NEITHER WORKS
#drinks.groupby('continent')[drinks.beer_servings > drinks.beer_servings.mean()].wine_servings.mean()
#drinks[groupby('continent').drinks.beer_servings > groupby('continent').drinks.beer_servings.mean()].wine_servings.mean()
#TWO ATTEMPTS.  NEITHER WORKS

#CLASS ANSWER - DOES THIS COMPARE EACH COUNTRY TO CONTINENTAL MEANS?
drinks[drinks.beer_servings > drinks.beer_servings.mean()].groupby('continent').wine_servings.mean()




''' Advanced Filtering '''

# loc: filter rows by LABEL, and select columns by LABEL
drinks.loc[0]   #rows with label 0 - index value is 0
drinks.loc[0:3]
drinks.loc[0:3, 'beer_servings':'wine_servings'] # Rows 0 to 3, returns beer_servings through wine_servings
drinks.loc[:, 'beer_servings':'wine_servings']
drinks.loc[[0, 3], ['beer_servings', 'spirit_servings']] #Rows 1 and 4, two columns


# iloc: filter rows by POSITION, and select columns by POSITION
drinks.iloc[0] #Row with 0th position (first row)
drinks.iloc[0:3]
drinks.iloc[0:3, 0:3] # rows and columns with positions 0 through 2
drinks.iloc[:, 0:3] #include all rows, and first three columns
drinks.iloc[[0,2],[0,1]] #return 1st and 3rd row, 1st and 2nd column


#mixing: select columns by LABEL, then filter by POSITION


