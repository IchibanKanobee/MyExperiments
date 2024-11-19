from nltk.tokenize import  word_tokenize
from nltk.corpus import stopwords


example_sentence = "This is an example showing stop words filtration."

stop_words = set(stopwords.words("english"))
#print (stop_words)

words = word_tokenize(example_sentence)
filtered_sentence = []

#for w in words:
#    if w not in stop_words:
#        filtered_sentence.append(w)

#print (filtered_sentence)

filtered_sentence = [w for w in words if not w in stop_words]
print (filtered_sentence)
