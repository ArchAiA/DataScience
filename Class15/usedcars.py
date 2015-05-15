# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:16:54 2015

@author: david
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/vehicles_train.csv')


#Explore the Data: Basic GroupBys
df.groupby('year').price.describe()
df.groupby('type').price.describe()
df.groupby('miles').price.describe()
df.groupby('doors').price.describe()
#Explore the Data: Basic GroupBys

#Explore the Data: Basic Charting
df.groupby(df.year).price.mean().plot(kind='bar')
df.groupby(df.miles).price.mean().plot(kind='bar')

df.groupby(df.year).price.plot(kind='box')



df.miles.hist()

df.plot(kind='scatter', x='miles', y='year', c='price', colormap='BuPu')
df[df.year < 2007].plot(kind='scatter', x='miles', y='year', c='price', colormap='BuPu')

df[df.year > 2006].price.mean()
df[(df.year < 2007) & (df.miles < 130000)].price.mean()
df[(df.year < 2007) & (df.miles > 130000)].price.mean()

df[df.year < 2007].describe()

df[df.miles < 130000].describe()
df[df.miles > 130000].describe()



#MSE By Hand
df1 = df[df.miles < 100000]
df2 = df[df.miles > 100000]

df1.price.mean()
df2.price.mean()
#MSE By Hand




#Building a Regression Tree in scit-kit learn Exercise
import pandas as pd
import numpy as np

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/vehicles_train.csv')
data['kind'] = data.type.map({'car':0, 'truck':1})

feat_cols = ['year', 'miles', 'doors', 'kind']

X = data[feat_cols]
y = data.price

from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor(random_state=1)

tree

from sklearn.cross_validation import cross_val_score
score = cross_val_score(tree, X, y, cv=3, scoring = 'mean_squared_error')

#RMSE CALCULATION
score
np.sqrt(-score)
np.mean(np.sqrt(-score))
#RMSE CALCULATION

#Class Predictions

from sklearn import metrics

y_test = [3000, 6000, 12000]
y_pred = [2214, 4500, 13500]
np.sqrt(metrics.mean_squared_error(y_test, y_pred))
#Class Predictions




#Building a Regression Tree in scit-kit learn Exercise









#Using a Loop to Find Desireable Depth
# define a range of values
max_depth_range = range(1, 11)

# create an empty list to store the average RMSE for each value of max_depth
RMSE_scores = []

# use cross-validation with each value of max_depth
for depth in max_depth_range:
    treereg = DecisionTreeRegressor(max_depth=depth, random_state=1)
    MSE_scores = cross_val_score(treereg, X, y, cv=3, scoring='mean_squared_error')
    RMSE_scores.append(np.mean(np.sqrt(-MSE_scores)))

# print the results
RMSE_scores
#Using a Loop to Find Desireable Depth



