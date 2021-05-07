

# Import the dataset
X = tweets_doc['Tweet']
Y = labels 



from sklearn.feature_extraction.text import TfidfVectorizer

tfid_vec = TfidfVectorizer(stop_words = 'english') 

X = tfid_vec.fit_transform(list(X)) #lower error comes here, so added list 



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



tweets_test = pd.read_csv('PA_test_tweets.txt',encoding = 'ISO-8859-1')

#tweets_test['Tweet']


# In[58]:


tfid_vec_test = tfid_vec.transform(list(tweets_test['Tweet']))


# In[61]:


# Test Predict 

test_predict = clf_tweet.predict(tfid_vec_test)


# In[62]:



# Output 


output = pd.DataFrame({'TweetID': tweets_test['TweetID'], 'Label': test_predict}, columns = ['TweetID', 'Label'])
output.head(100)


# In[68]:


# Convert to new file 

output.to_csv('hw2_output(new4).txt', header=True, index=None, sep=',', mode='a')

print(output)



