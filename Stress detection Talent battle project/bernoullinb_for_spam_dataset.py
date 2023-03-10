# -*- coding: utf-8 -*-
"""BernoulliNB For Spam Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_X8s4jIlPuIRoj2HMfGjCqKA2bvZj-Ll
"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer

#loading the dataset
df=pd.read_csv("/content/spam.csv",encoding="latin-1")

#getting first 5 records
df.head(10)

df.shape

#dropping unwanted columns
df=df.drop(["Unnamed: 2","Unnamed: 3","Unnamed: 4"],axis=1)

df.shape

#binarization
np.unique(df["class"])

np.unique(df["message"])

#vectorization
#creating sparse matrix using CountVectorizer
#converting df columns to individual array
x=df["message"].values
y=df["class"].values
#creating count vectorizer object
cv=CountVectorizer()
#transforming values
x=cv.fit_transform(x)
v=x.toarray()
#printing sparse matrix

#Data arrangement
#shifting target column to the end
first_col=df.pop('message')
df.insert(0,'message',first_col)
df

#train-test split=3:1
train_x=x[:4179]
train_y=y[:4179]
test_x=x[4179:]
test_y=y[4179:]

#training
bnb=BernoulliNB(binarize=0.0)
model=bnb.fit(train_x,train_y)
y_pred_train=bnb.predict(train_x)
y_pred_test=bnb.predict(test_x)

#results
print(bnb.score(train_x,train_y)*100)
print(bnb.score(test_x,test_y)*100)

#Classification reports
#for training set
from sklearn.metrics import classification_report
print(classification_report(train_y,y_pred_train))

#for testing set
from sklearn.metrics import classification_report
print(classification_report(test_y,y_pred_test))

