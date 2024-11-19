a, b = 0, 1
print(a)
print(b)

n = 5
for i in range(5):
    a, b = b, a+b
    print(b)
