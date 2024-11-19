#https://leetcode.com/problems/add-two-numbers/
class LinkedList:
    def __init__(self, number):
        self.number = number
        self.next = None

num1 = LinkedList(5)
num1.next = LinkedList(6)
num1.next = LinkedList(4)

num2 = LinkedList(7)
num2.next = LinkedList(0)
num1.next = LinkedList(8)

result = LinkedList(0)

while not num1.next is None:
    sum =
