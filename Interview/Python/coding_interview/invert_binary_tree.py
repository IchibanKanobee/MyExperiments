class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, node):
        if node is None:
            return None
        tmp = node.left
        node.left = node.right
        node.right = tmp
        self.invertTree(node.left)
        self.invertTree(node.right)
        return node




node = Node(4)
node.left = Node(2)
node.right = Node(7)

node.left.left = Node(1)
node.left.right = Node(3)

node.right.left = Node(6)
node.right.right = Node(9)

s = Solution()
inv = s.invertTree(node)

print(inv)