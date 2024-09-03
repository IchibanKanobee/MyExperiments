class Solution:
    # def longestCommonPrefix(self, words):
        # min_length = len(min(words, key=len))
        # for i in range(min_length):
        #     suffix = words[0][:i]
        #     for word in words:
        #         if suffix != word[:i]:
        #             return suffix
   def longestCommonPrefix(self, strs):
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


s = Solution()

words = ["flower","flow","flight"]

suff = s.longestCommonPrefix(words)
print (suff)

words = ["dog","racecar","car"]
suff = s.longestCommonPrefix(words)
print (suff)
