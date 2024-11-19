class Solution:
    def twoSum(self, nums, target):

        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i

        # An Upvote will be encouraging

nums = [2,7,11,15]
target = 9

s = Solution()
res = s.twoSum(nums, target)
print(res)
