#https://www.youtube.com/watch?v=C3Z9lJXI6Qw&t=0s&ab_channel=CoreySchafer

#Solution
class Sentence:
	def __init__(self, text):
		self.words = text.split(' ')
		count = len(self.words)
		self.start_index = 0
		self.end_index = count
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self):
		if (self.index >= self.end_index):
			raise StopIteration

		current = self.words[self.index]
		self.index += 1

		return current


def Word_Generator(text):
	words = text.split(' ')
	count = len(words)
	current = 0
	while (current < count):
		yield words[current]
		current += 1



#Problem
my_sentence = Sentence('This is a test')

for word in my_sentence:
	print(word)

my_word_generator = Word_Generator('This is a test')
for word in my_word_generator:
	print(word)