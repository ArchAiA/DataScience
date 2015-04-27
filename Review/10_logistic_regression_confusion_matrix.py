# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:01:25 2015

@author: david
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from math import exp
import numpy as np

#Read In Data
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/default.csv')
data.head()

# Change column to number for ['student']
data['student_bin'] = data.student.map({'No':0, 'Yes':1})
data.head()

# Let's do some cursory analysis.
data.groupby('default').balance.mean()
data.groupby('default').income.mean()

# Set X and y
feature_cols = ['balance', 'student_bin', 'income']
X = data[feature_cols]
y = data.default

X.head()
y.head()

# Train test split
X_train, X_test, y_train, y_text = train_test_split(X, y)

# Fit model
logreg = LogisticRegression() #Instantiating model
logreg.fit(X_train, y_train) #Fitting model
y_pred = logreg.predict(X_test) #Predicting with the fitted model


# Assess accuracy
print metrics.accuracy_score(y_test, y_pred)



'''NULL ACCURACY TESTS'''
#NULL ACCURACY RATE = 0.9732
#If we predict all zeroes for data.default, what were our
#accuracy score have been?
data.default.value_counts()
metrics.accuracy_score(y_test, [0]*len(y_test))
#If we had just predicted all zeroes, we would have scored higher

#ALTERNATIVE NULL ACCURACY RATE CALCULATION = 0.9732
y_test.mean()
1 - y_test.mean()
#Since filling in all zeroes for y_pred would mean 100% zeroes
#We can subtract y_test.mean() from 1 in order to perform
#the same null accuracy test



###############################################################################
### Intepretting Logistic Regression Coefficients
###############################################################################

# Let's look at the coefficients
#So... logreg.coef_ returns a list of lists, so we need logreg.coef_[0]
#in the loop to iterate over the inner list...
for col in zip(feature_cols, logreg.coef_[0]):
    print col[0], col[1]

# Let's interpret those.
for col in zip(feature_cols, logreg.coef_[0]):
    print 'A unit increase in', col[0], 'equals a', col[1], 'increase in odds.'
    
    
    

###############################################################################
### Confusion Matrix
###############################################################################

# Let's look at the confusion matrix
con_mat = metrics.confusion_matrix(y_test, y_pred)    
print con_mat 

true_neg = con_mat[0][0]
false_neg = con_mat[1][0]
true_pos = con_mat[1][1]
false_pos = con_mat[0][1]


# Sensitivity: percent of correct predictions when reference value is 'default'
#"How Many Of The True Positives Did We Identify?"
sensitivity = float(true_pos)/(false_neg + true_pos)
print sensitivity
#Alternate method of calculating sensitivity
metrics.recall_score(y_test, y_pred)


# Specificity: percent of correct predictions when reference value is 'not default'
#How Many Of The True Negatives Did We Identify?"
specificity = float(true_neg)/(false_neg + true_neg)
print specificity


###############################################################################
### Logistic Regression Thresholds
###############################################################################

# Logistic regression is actually predicting the underlying probability.  
# However, when you call the "predict" function, it returns class labels.  You
# can still predict the actual probability and set your own threshold if you'd
# like.  This can be useful in cases where the "signal" from the model isn't 
# strong.

# Predict probabilities
logreg.predict_proba(X_test) #This runs the probability model on the X_text data
probs = logreg.predict_proba(X_test)[:, 1] #This takes the probability that it is a positive, and puts it in the second column of the two dimensional array

# The natural threshold for probabilility is 0.5, but you don't have to use 
# that.

# Use 0.5 thrshold for predicting 'default' and confirm we get the same results
preds_05 = np.where(probs >= 0.5, 1, 0)
print metrics.accuracy_score(y_test, preds_05)
con_mat05 = metrics.confusion_matrix(list(y_test), list(preds_05))

# Let's look at a histogram of these probabilities.
plt.hist(probs, bins=20)
plt.title('Distribution of Probabilities')
plt.xlabel('Probabilities')
plt.ylabel('Frequency')
plt.show()

# Change cutoff for predicting default to 0.2
preds_02 = np.where(probs>=0.2, 1, 0)
delta = float((preds_02 != preds_05).sum())/len(X_test)*100
print 'Changing the threshold from 0.5 to 0.2 change %.2f percent of the predictions.' % delta


# Check the new accuracy, sensitivity, specificity
print metrics.accuracy_score(y_test, preds_02)
con_mat_02 = metrics.confusion_matrix(y_test, preds_02)
print con_mat_02
print 'Changing the threshold from 0.5 to 0.2 changes %.2f percent of the predictions.' % delta

# Let's define our true posititves, false positives, true negatives, and false negatives
true_neg = con_mat_02[0][0]
false_neg = con_mat_02[1][0]
true_pos = con_mat_02[1][1]
false_pos = con_mat_02[1][0]

sensitivity = float(true_pos)/(false_neg + true_pos)
print sensitivity
metrics.recall_score(y_test, preds_02)

specificity = float(true_neg)/(false_pos + true_neg)
print specificity
