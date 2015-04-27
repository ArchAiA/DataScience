# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:57:59 2015

@author: david
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics


trainData = pd.read_csv('test.csv')

#Basics
trainData.groupby('Sex').count()
trainData.groupby('Survived').count()
trainData.groupby('Survived').mean()
trainData.groupby('Pclass').count()
trainData.groupby('Pclass').mean()

trainData.groupby('Embarked').mean()

#Splitting survivors and those that died
survivors = trainData[trainData.Survived == 1]
dead = trainData[trainData.Survived == 0]


survivors.groupby('Sex').count()
survivors.groupby('Pclass').count()



pd.scatter_matrix(survivors)


trainData.Fare.hist(by=trainData.Survived, sharey=True, sharex=True)



#Split Apply Combine Attempt #1


df = trainData[(trainData.Age >= 0) & (trainData.Fare >= 0) & (trainData.Embarked >=0)]
df['male'] = df.Sex.map({'male':10, 'female':0})
df['departure'] = df.Embarked.map({'C':0, 'S':1, 'Q':2})


X = df[['Parch', 'Pclass', 'male', 'departure', 'Age']]
y = df.Survived


X_train, X_test, y_train, y_test = train_test_split(X, y)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X)
#print metrics.accuracy_score(y_test, y_pred)


#Survivors were slightly younger (mean)
#Survivors paid more per fare significantly (mean)
#Survivors tended to not have spouses/siblings on board slightly (mean)
#Survivors were much more likely to be a parent/child (mean)