#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeElement(self, nums, element):
        count = len(nums)
        for i in range(count-1, 0, -1):
            if nums[i] == element:
                del nums[i]
        return len(nums)

ls = [1,1,2, 2, 3]
s = Solution()
k = s.removeElement(ls, 2)
print(ls)
print(k)