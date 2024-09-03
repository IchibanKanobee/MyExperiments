class ListNode:
    def __init__ (self, val):
        self.val = val
        self.next = None

node_3 = ListNode(3)
node_2 = ListNode(2)
node_0 = ListNode(0)
node_min_4 = ListNode(-4)

node_3.next = node_2
node_2.next = node_0
node_0.next = node_min_4
node_min_4.next = node_2

node_5 = ListNode(5)

def if_has_cycle(node):
    path = []
    while (node.next is not None):
        path.append(node.val)
        next = node.next
        if next.val in path:
            return True
        node = next
    return False

print(if_has_cycle(node_3))
print(if_has_cycle(node_5))

def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

print(hasCycle(node_3))
print(hasCycle(node_5))

#chat gpt
def has_cycle(head):
    hare = head
    tortoise = head
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            return True
    return False