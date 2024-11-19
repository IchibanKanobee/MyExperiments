class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.next = two
two.next = three
three.next = four
four.next = five

def print_list(root):
    node = root
    while node is not None:
        print(node.val)
        node = node.next

print_list(one)

def reverse_list(root):
    current = root
    prev = None
    next = current.next
    while current is not None:
        new_current = current
        new_current.next = prev
        new_current.prev = next
        current = current.next

    return new_current

reversed = reverse_list(one)
print_list(reversed)
