#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

nums = [4,3,2,7,8,2,3,1]

#Output: [5,6]
s = set(range(1,10))
for num in nums:
    if num in s:
        s.remove(num)

print (s)