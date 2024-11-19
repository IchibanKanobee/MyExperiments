class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

start = ListNode(1)
start.next = ListNode(2)
start.next.next = ListNode(2)
start.next.next.next = ListNode(1)

def is_palindrome(node):
    forward = []
    reverse = []
    while node is not None:
        forward.append(node.val)
        node = node.next

    # temp = forward.copy()
    # while (len(temp) > 0):
    #     reverse.append(temp.pop())

    reverse = forward[::-1]

    if reverse == forward:
        return True
    else:
        return False

print (is_palindrome(start))