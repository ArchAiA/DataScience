# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 22:47:28 2015

@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt

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
#Mean Age: 27.56 which is older than the general mean, and only slightly lower than the general median
#Mean Pclass: 2.64 which is slightly a lower class ticket than the general mean
#Mean Survived: .2999 or 29.99% which is much lower than the general % that survived

#FOR PASSENGERS WITH CABIN NOTNULL
#Mean Fare: 76.14 which is far higher than the general mean AND Median Fare: 55.22 also much higher
#Mean Age: 35.83 which is far higher than the general mean AND Median Age: 36.00 also much higher
#Mean Pclass: 1.20 which is far higher than the general mean AND Median Pclass: 1.00 also much higher (over half had first class tickets)
#Mean Survived: 0.67 which is far higher than the general mean AND Median Survived: 1.0 also much higher



#Explore Age null values more deeply
df[df.Age.isnull()].describe()
df[df.Age.notnull()].describe()
df[df.Age.notnull()].describe() - df[df.Age.isnull()].describe()

#FOR PASSENGERS WITH AGE ISNULL


#Mean Survived: 



#USE KNN TO PREDICT AGE, AND THEN USE THAT DATASET TO PREDICT SURVIVED