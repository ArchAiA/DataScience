# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:09:42 2015

@author: David
"""

'''USING LINEAR REGRESSION TO FILL IN NULL VALUES FOR AGE'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split

import seaborn as sns
import statsmodels.formula.api as smf




df = pd.read_csv('train.csv')

df.shape
df.columns


### Using statsmodels ###
sns.pairplot(df, x_vars=['Fare', 'Survived', 'Pclass', 'SibSp', 'Parch'], y_vars='Age', size=7, aspect=0.7)

#Single Variable Linear Regression Model
lm1 = smf.ols(formula='Age ~ Fare', data=df).fit()
lm1.params
lm1.conf_int()
lm1.pvalues
lm1.rsquared
lm1.summary()
#Single Variable Linear Regression Model

lm2 = smf.ols(formula='Age ~ Fare + Pclass', data=df).fit()
lm2.params
lm2.conf_int()
lm2.pvalues
lm2.rsquared
lm2.summary()








































'''DENIGRATED: NOT GOING TO USE KNN TO FILL IN NULL VALUES FOR AGE'''
'''
#Fill in null values for Age by running KNN with sexcode, Fare, PClass, Survived
#Train and Test will be from Age notnull entries
#The fitted model will then be used on Age isnull entries


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split

df = pd.read_csv('train.csv')
#Change Sex to female:0, and male:1
df['sexcode'] = df.Sex.map({'male':0, 'female':1})

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
'''
'''DENIGRATED: NOT GOING TO USE TO FILL IN NULL VALUES FOR AGE'''