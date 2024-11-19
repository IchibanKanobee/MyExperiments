#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        count = len(nums)
        for i in range(count-1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i-1]
        return len(nums)
    #     n = len(nums)
    #     for i in range(n - 1, 0, -1):
    #         if (nums[i] == nums[i - 1]):
    #             nums.pop(i)
    #     return len(nums)

ls = [1,1,2, 2, 3]
s = Solution()
k = s.removeDuplicates(ls)
print(ls)
print(k)