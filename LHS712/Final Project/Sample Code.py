# -*- coding: utf-8 -*-
"""Task6.ipynb
"""


"""**Text Pre-processing**"""

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


def clean_tweets(tweet):
    tweet=str(tweet)
    tweet = tweet.lower()
    tweet=tweet.replace("{html}","") 
    remove_tweet = re.compile("<.*?>")
    remove_text = re.sub(remove_tweet, "", tweet)
    remove_url=re.sub(r"http\S+", "", remove_text)
    remove_num = re.sub("[0-9]+", "", remove_url)
    #since the word 'amp' is overlapping and we don't need it, we removed it.
    remove_words = re.sub(r'\bamp\b', '', remove_num)
    
    token = RegexpTokenizer(r"\w+")
    word_token = token.tokenize(remove_words)  
    filtered_tweet = [i for i in word_token if len(i) > 2 if not i in stopwords.words('english')]
    stemmer_tweet=[stemmer.stem(i) for i in filtered_tweet]
    lemmatizer_tweet=[lemmatizer.lemmatize(i) for i in stemmer_tweet]
    return " ".join(filtered_tweet)

train['tweet'] = train['tweet'].map(lambda s:clean_tweets(s)) 
valid['tweet'] = valid['tweet'].map(lambda s:clean_tweets(s))



"""**Creating training and test datasets**"""

train_x = train['tweet']
train_y = train['label']
test_x = valid['tweet']
test_y = valid['label']

# Encode target labels to numeric
# Lit-News_mentions = 0
# Nonpersonal_reports = 1
# Self_reports = 2
Encoder = LabelEncoder()
train_y = Encoder.fit_transform(train_y)
test_y = Encoder.fit_transform(test_y)

pd.crosstab(index=train_y,     # Make a crosstab
                      columns="prop", normalize='all')      # Name the count column

pd.crosstab(index=test_y,     # Make a crosstab
                      columns="prop", normalize='all')      # Name the count column

pd.crosstab(index=all_data['label'],     # Make a crosstab
                      columns="prop", normalize='all')      # Name the count column

"""**Feature Engineering: TFIDF**"""

Tfidf_vect = TfidfVectorizer(max_features=1000)
Tfidf_vect.fit(train_x)
train_x_tfidf = Tfidf_vect.transform(train_x)
test_x_tfidf = Tfidf_vect.transform(test_x)


# NB Classifier w/ Tfidf
nb_classifier_tfidf = naive_bayes.MultinomialNB()
nb_classifier_tfidf.fit(train_x_tfidf, train_y)
y_pred_nb_tfidf = nb_classifier_tfidf.predict(test_x_tfidf)
nb_tfidf_acc = metrics.accuracy_score(test_y, y_pred_nb_tfidf)
nb_tfidf_f1 = metrics.f1_score(test_y, y_pred_nb_tfidf, average = 'weighted')

print(metrics.classification_report(test_y, y_pred_nb_tfidf,
                                            target_names=['Lit-News_mentions', 'Nonpersonal_reports',
                                                          'Self_reports']))
print('------------------------------')
print("confusion matrix:")
print(metrics.confusion_matrix(test_y, y_pred_nb_tfidf))
print('------------------------------')
print("Number of mislabeled points out of a total %d points : %d" % (test_x_tfidf.shape[0], (test_y != y_pred_nb_tfidf).sum()))


"""**Random Forest**"""

# Random Forest with tfidf
rf_classifier_tfidf = RandomForestClassifier()
rf_classifier_tfidf.fit(train_x_tfidf, train_y)
y_pred_rf_tfidf = rf_classifier_tfidf.predict(test_x_tfidf)

rf_tfidf_acc = metrics.accuracy_score(test_y, y_pred_rf_tfidf)
rf_tfidf_f1 = metrics.f1_score(test_y, y_pred_rf_tfidf, average = 'weighted')

print(metrics.classification_report(test_y, y_pred_rf_tfidf,
                                            target_names=['Lit-News_mentions', 'Nonpersonal_reports',
                                                          'Self_reports']))
print('------------------------------')
print("confusion matrix:")
print(metrics.confusion_matrix(test_y, y_pred_rf_tfidf))
print('------------------------------')
print("Number of mislabeled points out of a total %d points : %d" % (test_x_tfidf.shape[0], (test_y != y_pred_rf_tfidf).sum()))

