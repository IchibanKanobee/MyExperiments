#https://www.youtube.com/watch?v=rW4vm0-DLYc&ab_channel=NeetCode

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        count = len(self.q)
        for i in range (count-1):
            x = self.q.popleft()
            self.q.append(x)
        return self.q.popleft()


    def top(self):
        return self.q[-1]

    def empty(self):
        return len(self.q) == 0