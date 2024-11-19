#binary sentiment analysis
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC


#documents = [(list(movie_reviews.words(fileid)), category)
#             for category in movie_reviews.categories()
#             for fileid in movie_reviews.fileids(category)]

documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
#        print (list(movie_reviews.words(fileid)))
#        print(category)
        documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)
#print(documents[1])

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


classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes accuracy :", (nltk.classify.accuracy(classifier, testing_set)) * 100)
classifier.show_most_informative_features(15)

save_classifier = open("naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()



mnb_classifier = SklearnClassifier(MultinomialNB()).train(training_set)
print("Multinomial binary accuracy :", (nltk.classify.accuracy(mnb_classifier, testing_set)) * 100)
#mnb_classifier.show_most_informative_features(15)

save_classifier = open("multinomial_binary.pickle", "wb")
pickle.dump(mnb_classifier, save_classifier)
save_classifier.close()



bernoulli_classifier = SklearnClassifier(BernoulliNB()).train(training_set)
print("Bernoulli accuracy :", (nltk.classify.accuracy(bernoulli_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("bernoulli.pickle", "wb")
pickle.dump(bernoulli_classifier, save_classifier)
save_classifier.close()






logistic_regression = SklearnClassifier(LogisticRegression()).train(training_set)
print("Logistic regression accuracy:", (nltk.classify.accuracy(logistic_regression, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("logistic_regression.pickle", "wb")
pickle.dump(logistic_regression, save_classifier)
save_classifier.close()




sgd_classifier = SklearnClassifier(SGDClassifier()).train(training_set)
print("SGD accuracy :", (nltk.classify.accuracy(sgd_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("sgd.pickle", "wb")
pickle.dump(sgd_classifier, save_classifier)
save_classifier.close()




svc_classifier = SklearnClassifier(SVC()).train(training_set)
print("SVC accuracy :", (nltk.classify.accuracy(svc_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("svc.pickle", "wb")
pickle.dump(svc_classifier, save_classifier)
save_classifier.close()




linear_svc_classifier = SklearnClassifier(LinearSVC()).train(training_set)
print("Linear SVC accuracy :", (nltk.classify.accuracy(linear_svc_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("linear_svc.pickle", "wb")
pickle.dump(linear_svc_classifier, save_classifier)
save_classifier.close()




nusvc_classifier = SklearnClassifier(NuSVC()).train(training_set)
print("NUSVC accuracy :", (nltk.classify.accuracy(nusvc_classifier, testing_set)) * 100)
#bernoulli_classifier.show_most_informative_features(15)

save_classifier = open("nusvc.pickle", "wb")
pickle.dump(nusvc_classifier, save_classifier)
save_classifier.close()