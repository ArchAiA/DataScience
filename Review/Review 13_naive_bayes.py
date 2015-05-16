
#Imports
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

#Read in the data
df = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/SMSSpamCollection.txt',
                   sep = '\t', header = None, names = ['label', 'msg'])
                   
       
#Explore data
df.isnull().sum()         
df.head()   
df.describe()
df.groupby('label').describe()


#Convert label to a binary value
df['label_bin'] = df.label.map({'ham':0, 'spam':1})


#Split into training, and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.msg, df.label_bin, random_state=1)

print X_train.shape, y_train.shape
print X_test.shape, y_test.shape





'''SIMPLE EXAMPLE'''
## COUNTVECTORIZER: 'convert text into a matrix of token counts'
vect = CountVectorizer() #Instantiate Model
#Simple Example
train_simple = ['call you tonight',
                'Call me a cab',
                'please call me... PLEASE!']
#Learn vocabulary of the training data
vect.fit(train_simple)
vect.get_feature_names() #Each of the words in train simple is now a feature, and has been placed into a vector

#Now we transform the training data into a dtm so that we can 
#get a count of the number of times each word shows up in the 
#training data
train_simple_dtm = vect.transform(train_simple)                
train_simple_dtm.toarray() #So each word in train simple has been
                           #given it's own column, and each 1 in
                           #the array means that the word shows
                           #up in each row of train_simple

#View the train dtm with column headers
pd.DataFrame(train_simple_dtm.toarray(), columns=vect.get_feature_names())

#Create a simple testing data set
test_simple = ["please don't call me"]
test_simple_dtm = vect.transform(test_simple)

test_simple_dtm.toarray() 
pd.DataFrame(test_simple_dtm.toarray(), columns=vect.get_feature_names())
'''SIMPLE EXAMPLE'''
                
                
                
#COUNTVECTORIZER IS USED TO CREATE FEATURES FROM TEXT                
                
'''REAL EXAMPLE: USING SMS DATA - Getting Vocabulary Counts'''
#Instantiate the model
vect = CountVectorizer()
#Learn the vocabulary (fit), and transform into dtm in one step
X_train_dtm = vect.fit_transform(X_train)
#Create an array of the dtm entries
X_train_arr = X_train_dtm.toarray()
#Transform test data into dtm
X_test_dtm = vect.transform(X_test)

#store feature names and examine
X_train_features = vect.get_feature_names()


#SIMPLE SUMMARIES
#Calculate teh number of tokens in the 0th message in X_train_arr
np.sum(X_train_arr[0, :])
#Count how many times the 0th toekn appears across all messages in X_train_arr
np.sum(X_train_arr[:,0])
#Count how many times EACH token appears across ALL messages in train_arr
np.sum(X_train_arr, axis=0)
#Create a DataFrame of tokens with their counts
train_token_counts = pd.DataFrame({'token':X_train_features, 'count':np.sum(X_train_arr, axis=0)})
train_token_counts.sort('count', ascending=False)
'''REAL EXAMPLE: USING SMS DATA - Getting Vocabulary Counts'''


'''MODEL BUILDING WITH NAIVE BAYES'''
#Import and Instantiate
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
#Fit
nb.fit(X_train_dtm, y_train) #This tells NB to fit the X_train_dtm features to the y_train response
#Predict
y_pred = nb.predict(X_test_dtm) #This tells NB to take that fitted model, and to use the X_test_dtm features to kick out a response and store that respones in y_pred
#For checking with a confusion matrix you want to have actual
#predictions (not predicted probabilities/predict_proba)
y_pred
#Check
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred)
print metrics.confusion_matrix(y_test, y_pred)

#Exercise: show the message text for the false positives
X_test[y_test < y_pred]
#Exercise: show the message text for the false negatives
X_test[y_test > y_pred]
#The condition statements in the two above lines of code 
#returns a series of booleans that will determine which
#results are returned from X_test
#ex. y_test < y_pred returns a list of booleans that determine which rows are shown
#really go ahead, try it: y_test < y_pred

#STILL DON"T BELIEVE ME, TRY THIS:
boolarray = np.array([False, True, True, True, True])
X_test[boolarray]
#THIS IS EXACTLY WHAT y_test < y_pred DOES, IT CREATES AN ARRAY
#OF BOOLEANS





#Predicting Probabilities: predict (poorly calibrated) probabilities and calculate AUC

#Use predict_proba when you are measuring your results using roc_auc
#or when working with imbalanced datasets

#So nb.predict_proba(X_test_dtm) gives probability of ham in the 0th column and probability of spam in the 1th column
y_prob = nb.predict_proba(X_test_dtm)[:,1] #Since we want the probability of spam, we want the 1th column for every row

#Test accuracy
print metrics.roc_auc_score(y_test, y_prob)



'''COMPARING NB TO LogReg'''
all_dtm = vect.fit_transform(df.msg)
logreg = LogisticRegression()

#FOR CROSS_VAL WE USE THE ENTIRE DATASET
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score

cross_val_score(nb, all_dtm, df.label_bin, cv=10, scoring='roc_auc').mean()
cross_val_score(logreg, all_dtm, df.label_bin, cv=10, scoring='roc_auc').mean()











