#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn
import sys
import matplotlib


# In[2]:


# Read data


# In[3]:


def read_file(f):
    data = open(f,'r').readlines()[1:]
    row_id = [i.split('\t')[0].strip() for i in data]
    data = [i.split('\t')[1].strip().split(' ') for i in data]
    return row_id,data


# In[4]:


row_id_text, texts = read_file('./REVIEW_TEXT.txt')
row_id_tags, tags = read_file('./REVIEW_LABELSEQ.txt')


# In[5]:


### INPUTS


# In[6]:


def word2features(txt, i):
    word = txt[i]
    features = {
    'bias': 1.0,
    'word.lower()': word.lower(),
    'word[-3:]': word[-3:],
    'word[-2:]': word[-2:],
    'word.isupper()': word.isupper(),
    'word.istitle()': word.istitle(),
    'word.isdigit()': word.isdigit(),
}
    
    if i > 0:
        word1 = txt[i-1][0]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
        })
    
    else:
        features['BOS'] = True
        
    if i < len(txt)-1:
        word1 = txt[i+1][0]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
        })
    
    else:
        features['EOS'] = True
        
        
    return features


def sent2features(txt):
    return [word2features(txt, i) for i in range(len(txt))]
def sent2labels(txt):
    return [label for token, postag, label in txt]
def sent2tokens(txt):
    return [token for token, postag, label in txt]


# In[7]:


X = [sent2features(i) for i in texts]
y = tags


# In[8]:


X


# In[9]:



# Train / Validation sets

from sklearn.model_selection import train_test_split

X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size = 0.2)


# In[ ]:





# In[10]:


# CRF MODEL

from sklearn_crfsuite import CRF

crf = CRF()


# In[11]:


# Training and prediction

crf.fit(X_train, y_train)
y_pred = crf.predict(X_validation)


# In[12]:


# CRF Result
from sklearn_crfsuite.metrics import flat_classification_report

report = flat_classification_report(y_validation, y_pred)
print(report)


# In[14]:


# output = pd.DataFrame({'ID': tweets_test['TweetID'], 'TAGSEQ': y_pred}, columns = ['Label'])
# output.head(100)


# In[ ]:





# In[ ]:




