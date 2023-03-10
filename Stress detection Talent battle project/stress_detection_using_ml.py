# -*- coding: utf-8 -*-
"""Stress Detection Using ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IBtfoaaTZSYRkZMgmGmd1LYrJxJEuVhE
"""

import numpy as np
import pandas as pd

path="/content/stress.csv"

#loading dataset using read_csv() function available in pandas
df=pd.read_csv(path)

#reading first 5 records using head()
df.head()

#The describe() method returns description of the data in the DataFrame.
df.describe()

#number of null values ineach column
df.isnull().sum()

#as we are working on textual data we need to pre process it 
#we are using nltk (natural language tool kit) of NLP
import nltk
import re
from nltk.corpus import stopwords
import string
nltk.download('stopwords')
stemmer=nltk.SnowballStemmer("english")
stopword=set(stopwords.words("english"))
def clean(text):
  #returns a string where all characters are lower case,symbols and numbers are ignored
  text=str(text).lower()
  #substring and returns a string with replaced values
  text=re.sub('\[.*?\]',' ',text)
  #white space character with pattern
  text=re.sub('https?://\S+/www\. \S+',' ',text)
  #special char enclosed in square brackets
  text=re.sub('<. *?>+', ' ',text)
  #eliminate punctuation from string
  text=re.sub(' [%s]' %re.escape(string.punctuation), ' ',text)
  text=re.sub(' \n',' ',text)
  #word character ASCII punctuation
  text=re.sub(' \w*\d\w*' , ' ',text)
  #remove stopwords
  text=[word for word in text.split(' ') if word not in stopword]
  text=" ".join(text)
  #remove morphological affixes from words
  text=[stemmer.stem(word) for word in text.split(' ')]
  text=" ".join(text)
  return text
df["text"]=df["text"].apply(clean)

#wordcloud
#To find the words which are frequently used the words that are used more are in large size
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS ,ImageColorGenerator
text=" ".join(i for i in df.text)
stopwords=set(STOPWORDS)
wordcloud=WordCloud( stopwords=stopwords,background_color="white").generate(text)
plt. figure(figsize=(15,10) )
plt. imshow(wordcloud,interpolation="bilinear")
plt. axis("off")
plt. show()

from sklearn. feature_extraction. text import CountVectorizer
from sklearn. model_selection import train_test_split
x= np.array(df["text"])
y= np.array(df["label"])
cv= CountVectorizer ()
X= cv. fit_transform(x)
xtrain,xtest,ytrain,ytest = train_test_split(X, y,test_size=0.33,random_state=42)

from sklearn.naive_bayes import BernoulliNB
#training the model
model=BernoulliNB()
model.fit(xtrain,ytrain)

y_pred_train=model.predict(xtrain)
y_pred_test=model.predict(xtest)

#results
print(model.score(xtrain,ytrain)*100)
print(model.score(xtest,ytest)*100)

#Classification reports
#for training set
from sklearn.metrics import classification_report
print(classification_report(ytrain,y_pred_train))

#for testing set
from sklearn.metrics import classification_report
print(classification_report(ytest,y_pred_test))

#Taking user input and checking whether a person is stressed or not
#1 indicates stress
#0 indicates no stress
user=input("Enter the text")
data=cv.transform([user]).toarray()
output=model.predict(data)
print(output)





















