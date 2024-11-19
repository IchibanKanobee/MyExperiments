#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

#nums = [-1,0,3,5,9,12], target = 9
#Output: 4

nums = [-1,0,3,5,9,12]

def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
            continue
        else:
            r = mid
    return -1

print (binary_search(nums, 7))