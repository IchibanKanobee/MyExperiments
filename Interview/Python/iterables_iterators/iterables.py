#Iterables means that it is something that can be looped over.

nums = [1,2,3]
for num in nums:
	print(num)

#All iterables have a method __iter__()
print (dir(nums))


i_nums = nums.__iter__()
i_nums = iter(nums) #same as above
print (dir(i_nums))

#nums.__iter__() will return an iterator. Iterator is an object with state that remembers where it is during iteration
#They also know how to get the next value by calling the __next__() method.
#All iterators have __iter__() method, so they are also iterables, but the method just returns self
print (next(i_nums))
print (next(i_nums))
print (next(i_nums))

#print (next(i_nums))
#If the iterator is exhausted (no more elements), it will throw StopIteration exception. Behind the scenes for loop uses the exception to iterate only through existing methos of the iterable

i_nums2 = iter(nums)
while (True):
	try:
		item = next(i_nums2)
		print (item)
	except StopIteration:
		break
#Iterators can only go forward
#Let's create an iterable class that behaves that range object
class MyRange():
	def __init__(self, start, end):
		self.value = start 
		self.end = end 

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		current = self.value 
		self.value += 1
		return current

nums = MyRange(1, 10)
for num in nums:
	print (num)

#print (next(nums))


#as generators
def my_range_as_generator(start, end):
	current = start 
	while current < end:
		yield current
		current += 1

my_range_gen = my_range_as_generator(1, 10)
for my_num in my_range_gen:
	print (my_num)

