import pickle, nltk
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression as LR
from sklearn.naive_bayes import BernoulliNB as BNB
from sklearn.ensemble import RandomForestClassifier as RForest
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from scipy.stats import mode

allowed_word_types = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP"]
stop_words = set(stopwords.words("english"))

open_file = open("Pickle/Vectorizer.pickle", "rb")
vectorizer = pickle.load(open_file)
open_file.close()

open_file = open("Pickle/LogisticRegression.pickle", "rb")
LR = pickle.load(open_file)
open_file.close()

#open_file = open("../Pickle/RandomForestClassifier.pickle", "rb")
#RForest = pickle.load(open_file)
#open_file.close()

open_file = open("Pickle/BernoulliNB.pickle", "rb")
BNB = pickle.load(open_file)
open_file.close()

def processing(tweet):
    tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',tweet)
    tweet = re.sub('@[^\s]+',' ', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    sentence = nltk.pos_tag(word_tokenize(str(tweet)))
    full = []
    for s in sentence:
        if s[1] in allowed_word_types and s[0] not in stop_words:
            full.append(s[0])
    fulls = " ".join(full)
    return fulls

#voted_classifier = VoteClassifier(LR, RForest)#RForest, BNB)

def sentiment(text):
    processed_text = processing(text);
    tfidf_vect = vectorizer.transform([processed_text]);
    yhatLR = LR.predict(tfidf_vect)
    yhatBNB = BNB.predict(tfidf_vect)
    modal = ((mode([yhatBNB, yhatLR])[0])[0])[0]
    average = ((yhatLR + yhatBNB)/2)[0]
    if average == 0:
        average = 1
    return modal, average