#[expression for element in iterable if condition]

a = [1,2,3]
b = [x**2 for x in a]
print (b)

c = [x**2 for x in a if x%2 == 0]
print(c)

#d = {k:v for k, v in iterable}
l = [(1, 2), (3, 4), (5, 6)]
e = {k**2:v**2 for k, v in l}
print(e)

