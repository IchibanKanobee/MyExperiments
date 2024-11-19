#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # lo = 0
        # hi = len(nums)-1
        # while lo <= hi:
        #     mid = (lo+hi)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         if lo == hi:
        #             return mid+1
        #         lo = mid+1
        #     else:
        #         if lo == hi:
        #             return mid
        #         hi = mid

        # lo = 0
        # hi = len(nums) - 1
        # while lo <= hi:
        #     mid = (lo + hi) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         if lo == hi:
        #             return mid + 1
        #         lo = mid + 1
        #     else:
        #         if lo == hi:
        #             return mid
        #         hi = mid

    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start

target = 4
nums = [1, 3, 5, 7]
s = Solution()
k = s.searchInsert(nums, target)
print(k)