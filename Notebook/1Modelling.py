#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random, nltk, pickle
from scipy.stats import mode
from statistics import mean
from nltk.tokenize import word_tokenize, sent_tokenize, WhitespaceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import ClassifierI
from sklearn.externals import joblib
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.svm import LinearSVC, NuSVC, SVC
import xgboost


# In[2]:


positive_doc = open("../Data/rt-polarity.pos", "r").read()
negative_doc = open("../Data/rt-polarity.neg", "r").read()


# In[3]:


stop_words = set(stopwords.words("English"))


# In[4]:


document = []
all_words = []


# In[5]:


allowed_word_types = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP"]


# In[6]:


tokenize = WhitespaceTokenizer()


# In[7]:


for p in positive_doc.split("\n"):
    document.append((p, "pos"))


# In[8]:


for n in negative_doc.split("\n"):
    document.append((n, "neg"))


# In[9]:


short_pos_words = tokenize.tokenize(positive_doc)
short_neg_words = tokenize.tokenize(negative_doc)


# In[10]:


for p in nltk.pos_tag(short_pos_words):
    if p[1] in allowed_word_types and p[0] not in stop_words:
        all_words.append(p[0].lower())


# In[11]:


for n in nltk.pos_tag(short_neg_words):
    if n[1] in allowed_word_types and n[0] not in stop_words:
        all_words.append(n[0].lower())


# In[12]:


all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:15000]


# In[13]:


def find_features(documents):
    words = word_tokenize(documents)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


# In[14]:


featuresets = [(find_features(rev), category) for (rev, category) in document]


# In[17]:


for i in range(0,5,1):
    random.shuffle(featuresets)
print(len(featuresets))


# In[18]:


training_set = featuresets[:7000]
testing_set = featuresets[7000:]


# In[ ]:


print("r")


# In[ ]:


LR = SklearnClassifier(LogisticRegression())
LR.train(training_set)
print("LogisticRegression Algo accuracy[%]: ", (nltk.classify.accuracy(LR, testing_set))*100)
save_classifier = open("../Pickled/LogisticRegression.pickle", "wb")
pickle.dump(LR, save_classifier)
save_classifier.close()


# In[ ]:


LR_params = {
    "penalty" : ["l1", "l2"],
    #"tol" : np.arange(0,1,0.0001),
    #"C" : np.arange(0,10,0.1),
    "random_state" : np.arange(0,100,1),
    #"solver" : ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    "max_iter" :  np.arange(0,200,1)
}
LR_search = GridSearchCV(estimator=LR, param_grid=LR_params, cv=5)
LR_search.fit(x_train,y_train)
print(LR_search.best_params_)


# In[20]:


BNB = SklearnClassifier(BernoulliNB())
BNB.train(training_set)
print("BernoulliNB Naive Bayes Algo accuracy[%]: ", (nltk.classify.accuracy(BNB, testing_set))*100)
save_classifier = open("../Pickled/BernoulliNB.pickle", "wb")
pickle.dump(BNB, save_classifier)
save_classifier.close()


# In[20]:


BNB_params = {
    #"alpha" : np.arange(0,100,1),
    "binarize" : np.arange(0,100,0.1)
}
Bernoulli_search = GridSearchCV(estimator=BNB, param_grid=BNB_params)
Bernoulli_search.fit(x_train,y_train)
print(Bernoulli_search.best_params_)


# In[21]:


save_doc = open("../Pickled/documents.pickle", "wb")
pickle.dump(document, save_doc)
save_doc.close()


# In[22]:


save_features = open("../Pickled/word_features.pickle", "wb")
pickle.dump(word_features, save_features)
save_features.close()


# In[17]:


classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes Algo accuracy[%]: ", (nltk.classify.accuracy(classifier, testing_set))*100)


# In[18]:


save_classifier = open("../Pickled/NaiveBayesClassifier.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

