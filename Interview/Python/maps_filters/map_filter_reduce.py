a = [1,2,3,4,5]
squares = map(lambda x: x*x , a)
for s in squares:
    print(s)
    

odds = filter(lambda x: x%2 != 0, a)
for o in odds:
    print(o)

