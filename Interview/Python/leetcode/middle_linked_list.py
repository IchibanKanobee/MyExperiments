class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

head = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
head.next = node_2
node_2.next = node_3
node_3.next = node_4
#node_4.next = node_5


def get_middle(head):
    slow = head
    fast = head
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
        if fast.next is None:
            return slow
        fast = fast.next
    return slow

mid = get_middle(head)
print (mid.val)