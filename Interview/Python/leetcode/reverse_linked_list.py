# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# start = ListNode(1)
# start.next = ListNode(2)
# start.next.next = ListNode(3)
# start.next.next.next = ListNode(4)
#
# node = start
#
# while node is not None:
#     print (node.val)
#     node = node.next
#
# current = start
# prev = None
# while current is not None:
#     tmp = current
#     current.next = prev
#     current = tmp.next
#
# print(1)

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# def reverse_linked_list(head: Node) -> Node:
#     prev = None
#     curr = head
#     while curr is not None:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#     return prev


def reverse_linked_list(head: Node) -> Node:
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


head = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
head.next = node_2
node_2.next = node_3
node_3.next = node_4

# Reverse the linked list
reversed_head = reverse_linked_list(head)

# Print the values of the reversed linked list
curr = reversed_head
while curr is not None:
    print(curr.val)
    curr = curr.next




