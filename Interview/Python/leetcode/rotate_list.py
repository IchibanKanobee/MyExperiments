class ListNode:
    def __init__ (self, val):
        self.val = val
        self.next = None



node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

#find the tail
#connect te tail with head
#move to l - k%l element
#break te next connection

k = 2
node = node_1
length = 1
while node.next is not None:
#    print(node.val)
    node = node.next
    length +=1

#print(length)
#print (node.val)
node.next = node_1

node = node_1
for i in range (length - k%length - 1):
    node = node.next

new_head = node.next
node.next = None

node = new_head
while node is not None:
    print(node.val)
    node = node.next


#
#
#
# while len(stack) > 0:
#     print(stack.pop().val)

#
# count = len(stack)
# index = count - 1 - k
# head_2 = stack[index]
# node_new = head_2
# for i in range(1, k):
#     node_new.next = stack[index + i]
#     node_new = node_new.next
#
#
# for i in range(k):
#     print(node.val)
#

