from nltk import sent_tokenize, word_tokenize

example_text = "The report by Mr. Smith from Colorado. The day care had a licensed capacity of six children, according to May 2019 data on the Colorado Department of Human Services website. The department immediately suspended the day care's license while it investigated, the agency said in a statement at the time."

print (sent_tokenize(example_text))

print (word_tokenize(example_text))

#for word in word_tokenize(example_text):
#    print (word)
