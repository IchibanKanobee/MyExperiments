#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

#Input: nums = [2,2,1]
#Output: 1

#use one-hot encoding
nums = [2,2,1]

def get_one_hot_vector_from_number(num):
    one_hot_vector = [0] * 60000
    one_hot_vector[num] = 1

def get_number_from_one_hot_vector(vector):
    for i in range(len(vector)):
        if vector[i] == 1:
            return i
    return 0

def find_single_number(nums):
    one_hot_vector = [0] * 60000
    for i in range(len(nums)):
        if one_hot_vector[nums[i]] == 0:
            one_hot_vector[nums[i]] = 1
        else:
            one_hot_vector[nums[i]] = 0
    return get_number_from_one_hot_vector(one_hot_vector)

print (find_single_number(nums))

#better solution - use xor
def singleNumber(nums): return reduce(lambda x,y: x^y, nums)