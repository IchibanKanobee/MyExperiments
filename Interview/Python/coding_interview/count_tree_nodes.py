nodeCount = 0

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, node):
        global nodeCount
        if not node is None:
            nodeCount += 1
            self.inOrder(node.left)
            self.inOrder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

s = Solution()
s.inOrder(root)
print(nodeCount)

