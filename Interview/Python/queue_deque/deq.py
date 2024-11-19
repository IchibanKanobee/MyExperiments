from collections import deque

de = deque([1, 2, 3, 4, 5, 6])
print (de)

de.pop()
print (de)

de.popleft()
print (de)

print (de.index(3))
print (de.count(3))
de.remove(3)
print (de)

de.insert(1,3)
print (de)
