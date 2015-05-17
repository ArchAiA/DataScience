#Cross validation takes a number of different samples
#So it is like running train_test_split multiple times
#In order to eliminate some of the high variance of the estimates
#Of out of sample predictions.
#So it runs the model several times, with different samples each time


#Imports
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




'''USING TRAIN TEST SPLIT'''
#Load in data
iris = load_iris()
X = iris.data
y = iris.target

#Using train/test/split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

#Check accuracy with KNN for n=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print metrics.accuracy_score(y_test, y_pred)

#How different will this be if we change to n=1
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print metrics.accuracy_score(y_test, y_pred)

#So we can see that the prediction will vary randomly...
'''USING TRAIN TEST SPLIT'''



'''The way that cross val resolves this is by running a bunch of 
train_test_split, and then averaging the results together'''



'''K-FOLD CROSS VALIDATION'''
'''     IRIS DATASET: MULTI-CLASS CLASSIFICATION'''
#In this case we are going to use cross_val to select tuning parameters
#     Load Iris Data
iris = load_iris()
X = iris.data
y = iris.target
#     10-fold cross_val with K=5
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
#     Use average accuracy as estimate of out of sample accuracy
print np.mean(scores)


#***     Search for optimal value of K
k_range = range(1,30)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores.append(np.mean(cross_val_score(knn, X, y, cv=10, scoring='accuracy')))

plt.plot(k_range, scores)

for i in k_range:
    print i, ":", scores[i-1]    #So 13 is the optimal n for prediction with 98.7% accuracy
#***     Search for optimal value of K

'''     IRIS DATASET: MULTI-CLASS CLASSIFICATION'''



'''     LOAN DEFAULT DATASET: USING CROSS_VAL TO SELECT BETWEEN MODELS FOR BINARY CLASSIFICATION'''
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/default.csv')
X = data[['balance']]
y = data.default

#10-fold cross_val with LogReg: roc_auc as metric
logreg = LogisticRegression()
y_pred02 = cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean()

#10-fold cross_val with knn: roc_acu as metric
knn = KNeighborsClassifier(n_neighbors = 5)
y_pred03 = cross_val_score(knn, X, y, cv=10, scoring='roc_auc').mean()
'''     LOAN DEFAULT DATASET: USING CROSS_VAL TO SELECT BETWEEN MODELS FOR BINARY CLASSIFICATION'''



'''     ADVERTISING DATASET: USING CROSS_VAL TO SELECT FEATURES FOR LINEAR REGRESSION'''
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)

#10-fold CROSS_VAL with 3 features: RMSE as metric
X = data[['TV', 'Radio', 'Newspaper']]
y = data.Sales

lm = LinearRegression()
scores = cross_val_score(lm, X, y, cv=10, scoring='mean_squared_error')
print scores

#Convert from MSE to RMSE
scores_sqrt = np.sqrt(-scores)
print scores_sqrt
print np.mean(scores_sqrt)

#CROSS_VAL with two features
feature_cols = ['TV', 'Radio']
X = data[feature_cols]
score = np.mean(np.sqrt(-cross_val_score(lm, X, y, cv=10, scoring='mean_squared_error')))
'''     ADVERTISING DATASET: USING CROSS_VAL TO SELECT FEATURES FOR LINEAR REGRESSION'''


#CROSS_VAL should be used for everything: tuning, choosing between
#models, choosing features, etc.  
#Just make sure to 1) choose a valid metric, 2)Use the entire dataset

'''K-FOLD CROSS VALIDATION'''

 








