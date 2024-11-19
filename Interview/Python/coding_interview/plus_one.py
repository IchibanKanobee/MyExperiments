class Solution:
    def addOneToFirstPosition(self, value):
        sum = value + 1
        if sum >= 10:
            return 0, 1
        else:
            return sum, 0

    def addOneToPosition(self, value, car:
        sum = value + car
        if sum >= 10:
            return 0, 1
        else:
            return sum, 0

    def plusOne(self, s: str) -> int:
        result = []
        count = len(s)
        sum, car = self.addOneToFirstPosition(int(s[count-1]))
        result.insert(0, sum)

        for i in range(count-2, -1, -1):
            res, car = self.addOneToPosition(int(s[i]), car, i)
            result.insert(0, res)
            if (i == 0) and (car == 1):
                result.insert(0, 1)
        return result

    # def plusOne(self, digits: List[int]) -> List[int]:
    #     s = ''.join([str(d) for d in digits])
    #     total = int(s) + 1
    #     return [int(i) for i in str(total)]

st = "988"
s = Solution()
l = s.plusOne(st)
print(l)