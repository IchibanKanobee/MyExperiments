# https://leetcode.com/problems/two-sum/
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

nums = [2,7,11,15]
target = 9
#Output: [0,1]

# sorted_nums = sorted(nums)
# print(sorted_nums)
# left = 0
# right = len(nums) - 1
#
# while (left < right):
#     if nums[left] + nums[right] == target:
#         print (left, right)
#         exit(0)
#     elif nums[left] + nums[right] < target:
#         left += 1
#         continue
#     else:
#         right -= 1
#         continue

d = {}
for i,num in enumerate(nums):
    if target-num in d:
        print( d[target-num], i)
        exit(0)
    d[num]=i