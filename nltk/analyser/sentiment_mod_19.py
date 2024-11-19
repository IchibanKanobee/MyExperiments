#binary sentiment analysis
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.tokenize import word_tokenize

from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        cl = mode(votes)
        return cl

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        cl = mode(votes)
        choice_votes = votes.count(cl)
        conf = choice_votes / len(votes)
        return conf


save_documents = open("pickled_models/documents.pickle", "rb")
documents = pickle.load(save_documents)
save_documents.close()

save_word_features = open("pickled_models/word_features_5k.pickle", "rb")
word_features = pickle.load(save_word_features)
save_word_features.close()

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


#print ((find_features((movie_reviews.words('neg/cv000_29416.txt')))))

save_featuresets = open("pickled_models/featuresets.pickle", "rb")
featuresets = pickle.load(save_featuresets)
save_featuresets.close()

random.shuffle(featuresets)

training_set = featuresets[:10000]
testing_set = featuresets[10000:]

save_classifier = open("pickled_models/naivebayes.pickle", "rb")
bayes_classifier = pickle.load(save_classifier)
save_classifier.close()


save_classifier = open("pickled_models/multinomial_binary.pickle", "rb")
mnb_classifier = pickle.load(save_classifier)
save_classifier.close()


save_classifier = open("pickled_models/bernoulli.pickle", "rb")
bernoulli_classifier = pickle.load(save_classifier)
save_classifier.close()


save_classifier = open("pickled_models/logistic_regression.pickle", "rb")
logistic_regression_classifier = pickle.load(save_classifier)
save_classifier.close()


save_classifier = open("pickled_models/sgd.pickle", "rb")
sgd_classifier = pickle.load(save_classifier)
save_classifier.close()


save_classifier = open("pickled_models/svc.pickle", "rb")
svc_classifier = pickle.load(save_classifier)
save_classifier.close()

save_classifier = open("pickled_models/linear_svc.pickle", "rb")
linear_svc_classifier = pickle.load(save_classifier)
save_classifier.close()


save_classifier = open("pickled_models/nusvc.pickle", "rb")
nusvc_classifier = pickle.load(save_classifier)
save_classifier.close()


voted_classifier = VoteClassifier(bayes_classifier,
                                  mnb_classifier,
                                  bernoulli_classifier,
                                  logistic_regression_classifier,
                                  sgd_classifier,
                                  svc_classifier,
#                                  linear_svc_classifier,
                                  nusvc_classifier)


def get_sentiment(text):
    features = find_features(text)
    return voted_classifier.classify(features), voted_classifier.confidence(features)