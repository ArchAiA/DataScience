# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:16:07 2015

@author: david
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1 Load the data
autos = pd.read_table('auto_mpg.txt', sep='|')
#autos = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.csv', sep='|')
# 1 Load the data





# 2A What is the shape of the data
print 'The dataframe has', autos.shape[0], 'rows, and', autos.shape[1], 'columns.'
# 2A What is the shape of the data


# 2B What variable ares available
print autos.columns #Lists dataframe headers (column names) in unicode
autos.describe #Prints out the data frame, and lists shape at the end
# 2B What variable ares available


# 2C For non numberic columns, what values are in the column?

# 2C For non numberic columns, what values are in the column?


# 2D What are the ranges for the values in each column? (Not Using iteritems)
'''
Deprecated for being STOOPID

autos.mpg.min()  
autos[['mpg']].max()

autos.cylinders.min()  
autos[['cylinders']].max()

autos.displacement.min()  
autos[['displacement']].max()

autos.horsepower.min()  
autos[['horsepower']].max()

autos.weight.min()  
autos[['weight']].max()

autos.acceleration.min()  
autos[['acceleration']].max()

autos.model_year.min()  
autos[['model_year']].max()

autos.origin.min()  
autos[['origin']].max()

autos.car_name.min()  
autos[['car_name']].max()

Deprecated for being STOOPID'''

#This is the easy answer for 2D...  Still would like to print out using 
#iteritems to make the output more human readable
autos.min()
autos.max()
# 2D What are the ranges for the values in each column? (Not Using iteritems)


# 2E What is the average for each column?  Does that differ significantly from the median?
autos.mean()
autos.median()
autos.mean() - autos.median()
# 2E What is the average for each column?  Does that differ significantly from the median?





# 3 Which 5 cars get the best gas mileage? Which 5 cars with more than 4 cylinders get the best gas mileage
autos.sort_index(by = 'mpg').tail(5)
autos[autos.cylinders > 4].sort_index(by='mpg').tail(5)
# 3 Which 5 cars get the best gas mileage? Which 5 cars with more than 4 cylinders get the best gas mileage





# 4 Which 5 cars get the worst gas mileage? Which cars with 4 or fewer cylinders get the worst gas mileage
autos.sort_index(by='mpg').head(5)
autos[autos.cylinders <= 4].sort_index(by='mpg').head(5)
# 4 Which 5 cars get the worst gas mileage? Which cars with 4 or fewer cylinders get the worst gas mileage





# 5 Use plots, groupby, aggregations, etc to explore the relationships
# between mpg and the other variables
autos.groupby('cylinders').mpg.mean().plot(kind='bar', title = 'Mean MPG by Cylinders')
plt.xlabel('Number of Cylinders in Automobile')
plt.ylabel('Mean Miles Per Gallon')
plt.show()


autos.plot(kind='scatter', x='model_year', y='mpg')
plt.show()

autos.groupby('model_year').mpg.mean().plot(kind='bar', title='Mean MPG by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Mean MPG')
plt.show()
# 5 Use plots, groupby, aggregations, etc to explore the relationships
# between mpg and the other variables


#SCRATCH
#for item in autos:
#    print item.mean()