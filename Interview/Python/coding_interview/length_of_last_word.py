class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
        
st = "Hello     world"
s = Solution()
l = s.lengthOfLastWord(st)
print(l)
