class Solution:
    def pivotIndex(self, nums):
        count = len(nums):
        total = sum(nums)
        leftSum = 0
        for i in range(count):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum


nums = [1, 7, 3, 6, 5, 6]
