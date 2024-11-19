#run this after scikit_learn_nltk_15.py so all pickle files are created
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

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



documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words_freq_dist = nltk.FreqDist(all_words)
#print(all_words_freq_dist.most_common(15))

#print (all_words_freq_dist["stupid"])

word_features = list(all_words_freq_dist.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


#print ((find_features((movie_reviews.words('neg/cv000_29416.txt')))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]


classifier_file = open("naivebayes.pickle", "rb")
bayes_classifier = pickle.load(classifier_file)
classifier_file.close()
print("Naive Bayes acuracy :", (nltk.classify.accuracy(bayes_classifier, testing_set)) * 100)
#classifier.show_most_informative_features(15)

classifier_file = open("multinomial_binary.pickle", "rb")
mnb_classifier = pickle.load(classifier_file)
classifier_file.close()
print("Multinomial binary acuracy :", (nltk.classify.accuracy(mnb_classifier, testing_set)) * 100)

classifier_file = open("bernoulli.pickle", "rb")
bernoulli_classifier = pickle.load(classifier_file)
classifier_file.close()
print("Bernoully acuracy :", (nltk.classify.accuracy(bernoulli_classifier, testing_set)) * 100)

classifier_file = open("logistic_regression.pickle", "rb")
logistic_regression_classifier = pickle.load(classifier_file)
classifier_file.close()
print("logistic regression acuracy :", (nltk.classify.accuracy(logistic_regression_classifier, testing_set)) * 100)

classifier_file = open("sgd.pickle", "rb")
sgd_classifier = pickle.load(classifier_file)
classifier_file.close()
print("SGD acuracy :", (nltk.classify.accuracy(sgd_classifier, testing_set)) * 100)

classifier_file = open("svc.pickle", "rb")
svc_classifier = pickle.load(classifier_file)
classifier_file.close()
print("SVC acuracy :", (nltk.classify.accuracy(svc_classifier, testing_set)) * 100)

#comment this to make the number of classifiers odd
#classifier_file = open("linear_svc.pickle", "rb")
#linear_svc_classifier = pickle.load(classifier_file)
#classifier_file.close()
#print("Liniear SVC acuracy :", (nltk.classify.accuracy(linear_svc_classifier, testing_set)) * 100)

classifier_file = open("nusvc.pickle", "rb")
nusvc_classifier = pickle.load(classifier_file)
classifier_file.close()
print("NuSVC acuracy :", (nltk.classify.accuracy(nusvc_classifier, testing_set)) * 100)

voted_classifier = VoteClassifier(bayes_classifier,
                                  mnb_classifier,
                                  bernoulli_classifier,
                                  logistic_regression_classifier,
                                  sgd_classifier,
                                  svc_classifier,
#                                  linear_svc_classifier,
                                  nusvc_classifier)
print("Voted acuracy :", (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)

print("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence: ", voted_classifier.confidence(testing_set[0][0]) * 100)
print("Classification:", voted_classifier.classify(testing_set[1][0]), "Confidence: ", voted_classifier.confidence(testing_set[1][0]) * 100)
print("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence: ", voted_classifier.confidence(testing_set[2][0]) * 100)
print("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence: ", voted_classifier.confidence(testing_set[3][0]) * 100)
print("Classification:", voted_classifier.classify(testing_set[4][0]), "Confidence: ", voted_classifier.confidence(testing_set[4][0]) * 100)
