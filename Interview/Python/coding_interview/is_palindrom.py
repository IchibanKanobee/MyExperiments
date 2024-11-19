class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp = x
        rev = 0
        while temp > 0:
            temp, n = divmod(temp, 10)
            rev = (rev * 10) + n

        if rev == x:
            return True
        else:
            return False



s = Solution()
print(s.isPalindrome(232))