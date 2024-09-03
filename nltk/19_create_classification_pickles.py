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



short_pos = open("short_reviews/positive.txt", encoding='latin-1').read()
short_neg = open("short_reviews/negative.txt", encoding='latin-1').read()

documents = []

all_words = []

#j is adjective, r is adverb, v is verb
allowed_word_types = ["J"]

for r in short_pos.split('\n'):
    documents.append((r, "pos"))
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for r in short_neg.split('\n'):
    documents.append((r, "neg"))
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

save_documents = open("pickled_models/documents.pickle", "wb")
pickle.dump(documents, save_documents)
save_documents.close()

#short_pos_words = word_tokenize(short_pos)
#short_neg_words = word_tokenize(short_neg)


#for w in short_pos_words:
#    all_words.append(w.lower())

#for w in short_neg_words:
#    all_words.append(w.lower())

all_words_freq_dist = nltk.FreqDist(all_words)

#print (all_words_freq_dist["stupid"])

word_features = list(all_words_freq_dist.keys())[:5000]

save_word_features = open("pickled_models/word_features_5k.pickle", "wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


#print ((find_features((movie_reviews.words('neg/cv000_29416.txt')))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]
save_featuresets = open("pickled_models/featuresets.pickle", "wb")
pickle.dump(featuresets, save_featuresets)
save_featuresets.close()


random.shuffle(featuresets)

training_set = featuresets[:10000]
testing_set = featuresets[10000:]



bayes_classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes accuracy :", (nltk.classify.accuracy(bayes_classifier, testing_set)) * 100)
bayes_classifier.show_most_informative_features(30)

save_classifier = open("pickled_models/naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()



mnb_classifier = SklearnClassifier(MultinomialNB()).train(training_set)
print("Multinomial binary accuracy :", (nltk.classify.accuracy(mnb_classifier, testing_set)) * 100)
#mnb_classifier.show_most_informative_features(15)

save_classifier = open("pickled_models/multinomial_binary.pickle", "wb")
pickle.dump(mnb_classifier, save_classifier)
save_classifier.close()



bernoulli_classifier = SklearnClassifier(BernoulliNB()).train(training_set)
print("Bernoulli accuracy :", (nltk.classify.accuracy(bernoulli_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("pickled_models/bernoulli.pickle", "wb")
pickle.dump(bernoulli_classifier, save_classifier)
save_classifier.close()


logistic_regression = SklearnClassifier(LogisticRegression()).train(training_set)
print("Logistic regression accuracy:", (nltk.classify.accuracy(logistic_regression, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("pickled_models/logistic_regression.pickle", "wb")
pickle.dump(logistic_regression, save_classifier)
save_classifier.close()



sgd_classifier = SklearnClassifier(SGDClassifier()).train(training_set)
print("SGD accuracy :", (nltk.classify.accuracy(sgd_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("pickled_models/sgd.pickle", "wb")
pickle.dump(sgd_classifier, save_classifier)
save_classifier.close()


svc_classifier = SklearnClassifier(SVC()).train(training_set)
print("SVC accuracy :", (nltk.classify.accuracy(svc_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("pickled_models/svc.pickle", "wb")
pickle.dump(svc_classifier, save_classifier)
save_classifier.close()


linear_svc_classifier = SklearnClassifier(LinearSVC()).train(training_set)
print("Linear SVC accuracy :", (nltk.classify.accuracy(linear_svc_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("pickled_models/linear_svc.pickle", "wb")
pickle.dump(linear_svc_classifier, save_classifier)
save_classifier.close()


nusvc_classifier = SklearnClassifier(NuSVC()).train(training_set)
print("NUSVC accuracy :", (nltk.classify.accuracy(nusvc_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("pickled_models/nusvc.pickle", "wb")
pickle.dump(nusvc_classifier, save_classifier)
save_classifier.close()


voted_classifier = VoteClassifier(bayes_classifier,
                                  mnb_classifier,
                                  bernoulli_classifier,
                                  logistic_regression_classifier,
                                  sgd_classifier,
                                  svc_classifier,
#                                  linear_svc_classifier,
                                  nusvc_classifier)
print("Voted acuracy :", (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)



def get_sentiment(text):
    features = find_features(text)
    return voted_classifier.classify(features), voted_classifier.confidence(features)