# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:09:42 2015

@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split


df = pd.read_csv('train.csv')

#Change Sex to female:0, and male:1
df['sexcode'] = df.Sex.map({'male':0, 'female':1})



#Fill in null values for Age by running KNN with sexcode, Fare, PClass, Survived
#Train and Test will be from Age notnull entries
#The fitted model will then be used on Age isnull entries

#Setting up the train/fitting datasets
dfAgeNotNull = df[df.Age.notnull()] #Cutting out all of the Age notnull for training
dfAgeNotNullX = dfAgeNotNull[['Survived', 'sexcode', 'Fare', 'Pclass']]
dfAgeNotNullY = dfAgeNotNull.Age #Cutting out target values for Age notnull for training

#Cutting up the train/fitting datasets for
X_train, X_test, y_train, y_test = train_test_split(dfAgeNotNullX, dfAgeNotNullY)

#Fitting the model
knn= KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test).astype(np.int64)
y_test = y_test.astype(np.int64)
print metrics.accuracy_score(y_test, y_pred)