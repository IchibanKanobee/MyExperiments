from collections import deque

queue = deque([])
print (queue)

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

val = queue.popleft()
print(val)
print(queue)

val = queue.popleft()
print(val)
print(queue)

val = queue.popleft()
print(val)
print(queue)
