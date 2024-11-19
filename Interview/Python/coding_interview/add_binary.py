def add_digits(d1, d2, car):
    res = d1 + d2 + car
    if res == 0:
        return 0, 0
    elif res == 1:
        return 1, 0
    elif res == 2:
        return 0, 1
    else:
        return 1, 1

def add_binary(a:str, b:str)->str:
    l1 = len(a)
    l2 = len(b)
    l - max(l1, l2)
    res = []
    car = 0
    while (a):
        d1 = int(a.pop())

    for i in range(l-1, -1, -1):
        d1 = a[i]
        d2 = b[i]
        d, car = add_digits(int(d1), int(d2), car)
        res.insert(0, d)
    if car == 1:
        res.insert(0, 1)
    s = [str(a) for a in res]
    res_str = "".join(s)
    return res_str

class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     carry = 0
    #     result = ''
    #
    #     a = list(a)
    #     b = list(b)
    #
    #     while a or b or carry:
    #         if a:
    #             carry += int(a.pop())
    #         if b:
    #             carry += int(b.pop())
    #
    #         result += str(carry %2)
    #         carry //= 2
    #
    #     return result[::-1]

    def addBinary(self, a:str, b:str)->str:
        res = ""
        car = 0
        a = list(a)
        b = list(b)
        while a or b or car:
            if a:
                car += int(a.pop())
            if b:
                car += int(b.pop())

            res += str(car % 2)
            car = car // 2

        return res[::-1]


a = "1011"
b = "1110"

#res = add_binary(a, b)
#print(res)

s = Solution()
print (s.addBinary(a, b))


