# class Solution:
#     def squareRoot(self, value):
#         delta = int(2e15)
#
#         for i in range(0, int(2e15)):
#
#             if i*i > value:
#                 return (i-1)
#             elif (i * i) == value:
#                 return i
#
class Solution:
  # def mySqrt(self, x: int) -> int:
  #   if x == 1:
  #     return 1
  #   right = x//2
  #   left = 0
  #   while left <= right:
  #     mid = (left + right)//2
  #     temp_product = mid*mid
  #     if temp_product == x:
  #       return mid
  #     elif temp_product > x:
  #       right = mid - 1
  #     elif temp_product < x:
  #       left = mid + 1
  #   return right

    def mySqrt(self, x):
        lo = 0
        hi = x // 2
        while (lo <= hi):
            mid = (hi + lo) // 2
            product = mid * mid
            if (product > x):
                hi = mid -1
            elif (product < x):
                lo = mid + 1
            else:
                return mid
        return hi

val = 34545989
s = Solution()
l = s.mySqrt(val)
print(l)
