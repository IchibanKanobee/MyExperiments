def square_numbers(nums):
	result = []
	for i in nums:
		result.append(i*i)
	return result

def square_numbers_comprehension(nums):
	return [num*num for num in nums]


numbers = [1,2,3,4,5]
my_nums = square_numbers(numbers)
print (my_nums)


my_nums_comprehension = square_numbers_comprehension(numbers)
print (my_nums_comprehension)


def generator_square_numbers(nums):
	for i in nums:
		yield (i*i)


gen = generator_square_numbers(numbers)
print (gen)

print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
#print (next(gen))

my_nums_gen = generator_square_numbers(numbers)

for num in my_nums_gen:
	print (num)

def generator_square_numbers_comprehension(nums):
	return ((num*num) for num in nums)

gen_comprehension = generator_square_numbers_comprehension(numbers)
print (gen_comprehension)

print (next(gen_comprehension))
print (next(gen_comprehension))
print (next(gen_comprehension))
print (next(gen_comprehension))
print (next(gen_comprehension))

#convert generator to list
my_list = list(generator_square_numbers_comprehension(numbers))
print (my_list)