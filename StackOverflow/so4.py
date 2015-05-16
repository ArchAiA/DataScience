

'''IMPORTS'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import os
'''IMPORTS'''


'''READING IN DATA'''
os.chdir('/home/david/projects/data/so')
df = pd.read_csv('train.csv', index_col=0)
'''READING IN DATA'''


'''FEATURE ENGINEERING'''
def MakeFeatures(filename):
    df['TitleLength'] = df.Title.apply(len)
    df['BodyLength'] = df.BodyMarkdown.apply(len)
    df['NumTags'] = df.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)
    df.rename(columns={'PostCreationDate':'PostDate', 'OwnerUserId':'UserId', 'ReputationAtPostCreation':'Reputation', 'OwnerUndeletedAnswerCountAtPostTime':'Answers'}, inplace=True)
    return df
'''FEATURE ENGINEERING'''


'''FEATURE ENGINEER (FOR COLUMN NAMES) FOR TRAIN AND TEST FILES'''
train = MakeFeatures('train.csv')
test = MakeFeatures('test.csv')
'''FEATURE ENGINEER (FOR COLUMN NAMES) FOR TRAIN AND TEST FILES'''


'''EXPLORE DATA'''
#train.plot(kind='scatter', x=train.NumTags, y=train.TitleLength, c=train.OpenStatus)
df.groupby(df.OpenStatus).describe()
#Reputation, PostId, BodyLength, OwnerUserId, and Answers matter

'''EXPLORE DATA'''


'''TRAIN_TEST_SPLIT'''
feat_cols = ['Reputation', 'PostId', 'BodyLength', 'UserId', 'Answers']
X = train[feat_cols]
y = train.OpenStatus

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
'''TRAIN_TEST_SPLIT'''




'''MODEL 01: LogReg'''
#Fit LogReg
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, y)
#Predict LogReg
y_pred = logreg.predict(X_test)
#Score LogReg
print metrics.accuracy_score(y_test, y_pred)
'''MODEL 01: LogReg'''



'''MODEL 02: CountVectorizer - Titles'''
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()

#Create New features/response
A_train, A_test, b_train, b_test = train_test_split(df.Title, df.OpenStatus)

#Learn the vocabulary of the data in train.title
A_train_dtm = vect.fit_transform(A_train)

#Transform the test data into a document-term matrix
A_test_dtm = vect.transform(A_test)

#List feature names
vect.get_feature_names


#Use the results from CountVectorizer to build a Naive Bayes Model
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(A_train_dtm, b_train)

y_pred = nb.predict(A_test_dtm)

#Compare predictions
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred)

'''MODEL 02: CountVectorizer - Titles'''
