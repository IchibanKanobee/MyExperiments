class Solution:
    def myAtoi(self, s):
        num = 0
        s = s.strip()
        negative = False
        if s[0] == '-':
            negative = True

        length = len(s)
        start = 0 if not negative else 1
        for i in range(start, length):
            ch = s[i]
            prev_num = num
            num = num * 10 + int(ch)

            if not negative and num > 2e31 - 1:
                return prev_num

            if not negative and num > 2e31:
                return -prev_num

        if negative:
            num = -num

        return num


st = "        123345924597245720945790274525429879874578243598724059720458972094857295"

s = Solution()
num = s.myAtoi(st)
print (num)



