class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def hasCycle(self, node):
#        try:
        #     slow = head
        #     fast = head.next
        #     while slow is not fast:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return True
        # except:
        #     return False
        node_set = set()
        while node:
            if node in node_set:
                return True
            node_set.add(node)
            node = node.next
        return False

node = Node(3)
node.next = Node(2)
node.next.next = Node(0)
node.next.next.next = Node(-4)
#node.next.next.next.next = node.next


head = [3,2,0,-4]
pos = 1

s = Solution()
res = s.hasCycle(node)
print(res)
