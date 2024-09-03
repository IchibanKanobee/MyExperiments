class Solution:
    def isValid(self, symbols):
        symbol_stack = []
        openBrackets = ['(', '[', '{']
        matchingBrackets = {")" : "(", "]":"[", "}":"{"}
        for idx, symbol in enumerate(symbols):
            if symbol in openBrackets:
                symbol_stack.append(symbol)
            elif matchingBrackets[symbol] == symbol_stack[-1]:
                    symbol_stack.pop()
            else:
                return False
        return True


s = Solution()

str = "[]{}()"
res = s.isValid(str)
print (res)

str = "[{]]()"
res = s.isValid(str)

print(res)
