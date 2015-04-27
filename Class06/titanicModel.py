# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:09:51 2015

@author: David
"""

'''IMPORTS'''
#Core Data Analysis Imports
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.cross_valdation import train_test_split
#Linear Regression Imports
from sklearn.linear_model import LinearRegression

#Testing
from sklearn import metrics
'''IMPORTS'''





df = pd.read_csv('train.csv')



###Dealing with Null Values###
df.isnull().sum() #Null values in Age, Cabin, and Embarked



##Null Values: Embarked##
df[df.Embarked.isnull()]
df.Embarked.value_counts()
df[df.Pclass == 1].groupby(df.Embarked).mean()
#!Screw this.  I googled it, and Martha Evelyn Stone, and her maid
#!boarded the Titanic at Southampton

df['Embarked'].fillna('S', inplace=True)
df[df.Ticket == '113572'] #Check that the right NaNs were changed
##Null Values: Embarked##



##Null Values: Age##
#Basic Data Exploration
df.groupby('Age').Survived.mean()
df.groupby('Age').Fare.mean()
df.groupby('Age').Pclass.mean()
df.groupby('Survived').Age.plot(kind='hist', alpha=0.2)

#Creating Dummy Variables for Pclass
PclassDummies = pd.get_dummies(df.Pclass, prefix='Pclass').iloc[:, 1:]

'''FORGOT TO REMOVE FIRST COLUMN OF DUMMY VARIABLE
df = pd.concat([df, PclassDummies], axis=1) 
del df['Pclass_3']
del df['Pclass_2']
del df['Pclass_1']
FORGOT TO REMOVE FIRST COLUMN OF DUMMY VARIABLE'''

df = pd.concat([df, PclassDummies], axis = 1)

#Fitting Linear Models for Null Age Values
#First we are going to try linear regression to fillin Null values for Age
dfAgeNotNull = df[df.Age.notnull()]
dfAgeNotNullX = df[df.Age.notnull()][['Fare', 'Survived', 'Pclass']]
dfAgeNotNullY = df[df.Age.notnull()][['Fare', 'Survived', 'Pclass']]

X_train, X_test, y_train, y_test = train_test_split(dfAgeNotNullX, dfAgeNotNullY)
lmAge = LinearRegression()
lmAge.fit(X_train, y_train)
y_pred = lmAge.predict(X_test)
print np.sqrt(metrics.mean_squared_error(y_test, y_pred))