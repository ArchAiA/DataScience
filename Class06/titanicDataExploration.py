# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 22:47:28 2015

@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('train.csv')




'''Exploring The Data'''
#Count the number of null values in the dataframe
df.isnull().sum()   #Summarize null values per category
df.shape            #Return the general shape of the dataframe
df.describe()       #Return summary statistics for the dataframe

#FOR ALL PASSENGERS
#Mean Fare: 32.20 AND Median: 14.454 AND Middle 50%: 7.91 to 31.00
#Mean Age: 20.70 AND Median: 28.0 AND Middle 50%: 20.13 to 38.0
#Mean Pclass: 2.31
#Mean Survivied: .3838 MEANING 38.38% survived
'''Exploring The Data'''


'''Explore null values more deeply'''
df[df.Cabin.isnull()]       #Return rows where Cabin isnull
df[df.Age.isnull()]         #Return rows where Age isnull
df[df.Embarked.isnull()]    #Return rows where Embarked isnull.  For Embarked isnull, notice that the two null values shared the same Cabin, Ticket, were not parent/child, or siblings, and paid the same fare


#Explore Cabin null values more deeply - THIS IS IMPORTANT - THERE IS A SIGNIFICANT DIFFERENCE BETWEEN THOSE THAT HAVE NULLS FOR CABIN AND THOSE THAT DO NOT HAVE NULLS
df[df.Cabin.isnull()].describe()    #People with Cabin isnull were 1) less likely to survive, 2) had lower class tickets, 3) tended to be younger (mean of 27.56), and 4) Paid less than the mean fare
df[df.Cabin.notnull()].describe()   
df[df.Cabin.notnull()].describe() - df[df.Cabin.isnull()].describe() #Difference between notnull and null values for Cabin
#FOR PASSENGERS WITH CABIN ISNULL
#Mean Fare: 19.16 which is far less than the general mean, but higher than the general median
#Mean Age: 27.56 which is than the general mean, and only slightly lower than the general median
#Mean Pclass: 2.64 which is slightly a lower class ticket than the general mean
#Mean Survived: .2999 or 29.99% which is much lower than the general % that survived

#FOR PASSENGERS WITH CABIN NOTNULL
#Mean Fare: 76.14 which is far higher than the general mean AND Median Fare: 55.22 also much higher
#Mean Age: 35.83 which is far higher than the general mean AND Median Age: 36.00 also much higher
#Mean Pclass: 1.20 which is far higher than the general mean AND Median Pclass: 1.00 also much higher (over half had first class tickets)
#Mean Survived: 0.67 which is far higher than the general mean AND Median Survived: 1.0 also much higher

#Comparing CABIN NOTNULL to CABIN ISNULL
#Mean Fare: Those that have CABIN ISNULL paid 12.19 units less by mean, and 16.50 units less by median
#Mean Age: Those that have CABIN ISNULL were 8.27 years younger by mean and 10.00 years younger by median
#Mean Pclass: Those that have CABIN ISNULL tended to be in lower class cabins (1.44 lower by mean, and 2.00 by median)
#Mean Survived: Those that have CABIN ISNULL were less likley to survive. 




#Explore Age null values more deeply
df[df.Age.isnull()].describe()
df[df.Age.notnull()].describe()
df[df.Age.notnull()].describe() - df[df.Age.isnull()].describe()

#FOR PASSENGERS WITH AGE ISNULL
#Mean Fare: Those with age ISNULL paid 22.16 which is less than the general mean, and 8.05, again far less by median
#Mean Pclass: Those with age ISNULL tended to have a slightly lower class cabin (2.60), and a median of 3.00, and more than 75% had a 3rd class ticket
#Mean Survived: THos with age ISNULL had a far less chance of surviving, with 29.38% surviving by mean, and more than half did not survive

#FOR PASSENGERS WITH AGE NOTNULL
#Mean Fare: Very closely matched the general numbers for mean, and median
#Pclass: Very closely matched the mean, and median Pclass (2.24%), and (2.0)
#Survived: Very closely matched the general survival rate (40.62%) by mean.

#COMPARING PASSENGERS WITH AGE NOTNULL TO PASSENGERS ISNULL
#Fare: ISNULL paid 12.54 less by mean, and 7.69 less by  median
#Pclass: ISNULL were in a slightly higher class by mean, and by median... <REREAD>
#Survived: ISNULL were less likely to survive by mean (difference of 11.24% by mean)

'''SURVIVAL BY FIRST CHARACTER OF TICKET.  THIS IS IMPORTANT'''
#What were the survival rates by the first letter of each ticket
df.groupby(df.Ticket.str[:1]).Survived.count()
df.groupby(df.Ticket.str[:1]).Survived.sum()
df.groupby(df.Ticket.str[:1]).Survived.sum() / df.groupby(df.Ticket.str[:1]).Survived.count()
'''SURVIVAL BY FIRST CHARACTER OF TICKET.  THIS IS IMPORTANT''' 
'''ANS: I THINK THAT THE NUMBERS ARE JUST SMALL SO IT CAN SEEM SIG WHEN IT ISNT'''



'''Explore Age Null Values by Sex'''
df[df.Age.isnull()].groupby('Sex').Survived.mean()
df[df.Age.notnull()].groupby('Sex').Survived.mean()

df[df.Age.isnull()].groupby('Sex').count()
df[df.Age.isnull()].groupby('Sex').sum()
#Those with a NULL value for age were 8% points more likely to die than those with NOTNULL values for either Sex
'''Explore Age Null Values by Gender'''



'''GRAPHING'''
df[df.Age.notnull()].plot(kind='scatter', x='Age', y='Fare')

df.groupby(df.Age).Survived.mean().plot(kind='bar')
df.plot(kind='scatter', x='Fare', y='Age')


headers = df.columns.values
for header in headers:
    print header
    df[df.Age.notnull()].groupby('Age')[header].mean()



#USE KNN TO PREDICT AGE, AND THEN USE THAT DATASET TO PREDICT SURVIVED