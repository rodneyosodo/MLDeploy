import random, nltk
import pickle
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from nltk.classify import ClassifierI
from scipy.stats import mode
from statistics import mean
from nltk.tokenize import word_tokenize

class VoteClassifier(ClassifierI):
 	"""docstring for VoteClassifier"""
 	def __init__(self, *classifiers):
 		self._classifiers = classifiers
 	
 	def classify(self, features):
 		votes = []
 		for c in self._classifiers:
 			v = c.classify(features)
 			votes.append(v)
 		return (mode(votes)[0][0])

 	def confidence(self, features):
 		votes =[]
 		for c in self._classifiers:
 			v = c.classify(features)
 			votes.append(v)
 		choice_votes = int(mode(votes)[1])
 		conf = choice_votes / len(votes)
 		return conf

documents_f = open("Pickled/documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()

word_features_f = open("Pickled/word_features.pickle", "rb")
word_features = pickle.load(word_features_f)
word_features_f.close()


def find_features(documents):
    words = word_tokenize(documents)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

open_file = open("Pickled/NaiveBayesClassifier.pickle", "rb")
NaiveB = pickle.load(open_file)
open_file.close()

open_file = open("Pickled/BernoulliNB.pickle", "rb")
BNB = pickle.load(open_file)
open_file.close()

open_file = open("Pickled/LogisticRegression.pickle", "rb")
LR = pickle.load(open_file)
open_file.close()

voted_classifier = VoteClassifier(NaiveB, BNB, LR)

def sentiment(text):
	feats = find_features(text)
	return voted_classifier.classify(feats), voted_classifier.confidence(feats)