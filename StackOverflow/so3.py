# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:39:55 2015

@author: David
"""
#Import Modules
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.cross_validation import train_test_split

#Read In Data
#os.chdir('../../../../Sites/data/so/')
os.chdir('/home/david/projects/data/so/')
df = pd.read_csv('train.csv', index_col=0)


# Helper code for class 17 exercise

# define the function
def make_features(filename):
    df = pd.read_csv(filename, index_col=0)
    df.rename(columns={'OwnerUndeletedAnswerCountAtPostTime':'Answers'}, inplace=True)
    df['TitleLength'] = df.Title.apply(len)
    df['BodyLength'] = df.BodyMarkdown.apply(len)
    df['NumTags'] = df.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)
    return df

# apply function to both training and testing files
train = make_features('train.csv')
test = make_features('test.csv')

# define X and y
feature_cols = ['ReputationAtPostCreation', 'Answers', 'TitleLength', 'BodyLength', 'NumTags']
X = train[feature_cols]
y = train.OpenStatus

###############################################################################
##### Create some models with the derived features
############################################################################### 


###############################################################################
##### Count vectorizer
###############################################################################


# define X and y
X = train.Title
y = train.OpenStatus

# split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# use CountVectorizer with the default settings
#from sklearn.feature_extraction.text import CountVectorizer
#vect = CountVectorizer()

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()


# fit and transform on X_train, but only transform on X_test

#Learn the Vocabulary of the Training Data
train_dtm = vect.fit_transform(X_train)
test_dtm = vect.transform(X_test)
vect.fit(X_train)

#Examine the vocabulary and document-term matrix together
pd.DataFrame(train_dtm.toarray(), columns=vect.get_feature_names())


###############################################################################
##### Create a model with the text features
###############################################################################