from collections import deque

class MyStack:
    def __init__(self):
        self.deq = deque()

    def push(self, x):
        self.deq.append(x)

    def pop(self):
        x = self.deq.pop()
        return x

    def top(self):
        return self.deq[-1]

    def empty(self):
        return self.deq.count == 0


myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)

print(myStack.top())
print(myStack.empty())

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())



