from nltk.stem import  PorterStemmer
from nltk.tokenize import word_tokenize


ps = PorterStemmer()

#example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

#for w in example_words:
#    print(ps.stem(w))


new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
new_text = "I'd like to introduce my collegue. I know Jennifer for 20 years."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

