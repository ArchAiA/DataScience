# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:39:03 2015

@author: david
"""

'''Read in the data, and assign column names'''
import pandas as pd
col_names = ['slength', 'swidth', 'plength', 'pwidth', 'species']
iris = pd.read_csv('iris.data', names = col_names)



'''Explore the shape of the data'''
iris.shape #Number of columns and rows in the data
iris.describe() #Summary stats (mean, max, min, quartiles)
#iris.groupby('species').count() #THis info shows up in the groupby-describe
iris.groupby('species').describe()
iris.boxplot(by='species')

iris.isnull().sum() #Gives a count of the null values



'''Transform species into a numeric categorical value'''
iris['species_num'] = iris.species.map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})



'''Create X, and then create y'''
X = iris[['slength', 'swidth', 'plength', 'pwidth']]
y = iris.species_num



'''Predict y using KNN'''
from sklearn.neighbors import KNeighborsClassifier
knn =  KNeighborsClassifier(n_neighbors = 5)
knn.fit(X, y)
knn.predict([3, 5, 6, 7])



'''This is wrong.  I need to use some kind of apply or something on the
original iris object

for index, row in iris.iterrows():
    row['prediction'] = knn.predict([row['slength'], row['swidth'], row['plength'], row['pwidth']])
    #iris[row]['prediction'] = knn.predict([row['slength'], row['swidth'], row['plength'], row['pwidth']])
'''