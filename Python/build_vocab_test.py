import collections

data = ['apple', 'chair', 'bed', 'apple', 'chair', 'chair', 'chair', 'bed', 'bed']
counter = collections.Counter(data)
print counter

count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
print count_pairs

words, c = list(zip(*count_pairs))
print words
print c

l = len(words)
print l

r = range(len(words))
print r 

word_to_id = dict(zip(words, range(len(words))))
print word_to_id

id_to_word = dict(zip(range(len(words)), words))
print id_to_word
