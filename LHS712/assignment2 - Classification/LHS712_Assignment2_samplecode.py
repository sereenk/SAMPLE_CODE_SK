#!/usr/bin/env python
# coding: utf-8

# In[35]:


import os
import re
import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
import string
from sklearn import preprocessing

import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from scipy.io import arff
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer


# In[50]:


# Import the dataset


label_doc = pd.read_csv('PA_training_labels.txt')

tweet_id = label_doc['TweetID']
labels = label_doc['Label']

tweets_doc = pd.read_csv('PA_training_tweets.txt',encoding = 'ISO-8859-1')

X = tweets_doc['Tweet']
Y = labels 


# In[51]:


# 1. Lowercase text
#2. Remove whitespace
#3. Remove numbers
#4. Remove special characters
#5. Remove emails
#6. Remove stop words
#7. Remove NAN
#8. Remove weblinks
#9. Expand contractions (if possible not necessary)
#10. Tokenize

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


def tweet_clean(text):
    text=str(text)
    text = text.lower()
    text=text.replace('{html}',"") 
    cleantweet = re.compile('<.*?>')
    cleantext = re.sub(cleantweet, '', text)
    remove_url=re.sub(r'http\S+', '',cleantext)
    remove_num = re.sub('[0-9]+', '', remove_url)
    token = RegexpTokenizer(r'\w+')
    twt_tokens = token.tokenize(remove_num)  
    filtered_tweets = [i for i in twt_tokens if len(i) > 2 if not i in stopwords.words('english')]
    stem_tweets=[stemmer.stem(i) for i in filtered_tweets]
    lemma_tweets=[lemmatizer.lemmatize(i) for i in stem_tweets]
    return " ".join(filtered_tweets)
    
tweets_doc['Tweet'] = tweets_doc['Tweet'].map(lambda s:tweet_clean(s))



# In[ ]:


#Cleaning 

#1. Cleaning_1 : Removing HTTP
   
#tweets_doc['Tweet'] = tweets_doc['Tweet'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])

#tweets_doc['Tweet'][1210]


# In[ ]:


#2. Cleaning_2: removing punctuations
#string.punctuation

#def without_punct(text):
    #text  = "".join([char for char in text if char not in string.punctuation])
    #text = re.sub('[0-9]+', '', text)
    #return text

#tweets_doc['Tweet'] = tweets_doc['Tweet'].apply(lambda x: without_punct(x))

#tweets_doc['Tweet'][1210]


# In[ ]:





# In[52]:


from sklearn.feature_extraction.text import TfidfVectorizer

tfid_vec = TfidfVectorizer(stop_words = 'english') 

X = tfid_vec.fit_transform(list(X)) #lower error comes here, so added list 


# In[53]:


# Splitting the Data

X_training, X_validation, Y_training, Y_validation = train_test_split(X, Y, test_size=0.3, random_state=0)


# In[54]:


#Linear SVC

from sklearn.svm import LinearSVC

clf_tweet = LinearSVC(class_weight='balanced')

clf_tweet.fit(X_training,Y_training)


# In[55]:


# Predict

Y_prediction = clf_tweet.predict(X_validation)


# In[56]:


# Classification report

print(classification_report(Y_validation,Y_prediction))


# In[ ]:





# In[57]:


# Checking tweets test file

tweets_test = pd.read_csv('PA_test_tweets.txt',encoding = 'ISO-8859-1')

#tweets_test['Tweet']


# In[58]:


tfid_vec_test = tfid_vec.transform(list(tweets_test['Tweet']))


# In[61]:


# Test Predict 

test_predict = clf_tweet.predict(tfid_vec_test)


# In[62]:


# Trying another model : Random Forest Model

from sklearn.ensemble import RandomForestClassifier

rfc_model = RandomForestClassifier()


rfc_model.fit(X_training, Y_training)

rfc_pred = rfc_model.predict(X_validation)


# In[63]:


## Checking Accuracy _ Random Forest Model
from sklearn import metrics

metrics.accuracy_score(Y_validation,rfc_pred) 


# In[64]:


# Checking f-1 score _ Random Forest Model

metrics.f1_score(Y_validation,rfc_pred, average = 'micro')  # Macro shows lower value, so don't use that


# In[65]:


# Classification report : Random Forest

print(classification_report(Y_validation,rfc_pred))


# In[66]:


# Checking for a another new model:




# In[67]:


# Output 


output = pd.DataFrame({'TweetID': tweets_test['TweetID'], 'Label': test_predict}, columns = ['TweetID', 'Label'])
output.head(100)


# In[68]:


# Convert to new file 

output.to_csv('hw2_output(new4).txt', header=True, index=None, sep=',', mode='a')

print(output)


# In[ ]:





# In[ ]:




