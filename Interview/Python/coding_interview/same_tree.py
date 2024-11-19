class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, root1, root2):
            if root1 is None and root2 is None:
                return True
            if not root1 is None or not root2 is None:
                return False

            if root1.value != root2.value:
                return False
            if not self.isSameTree(root1.left, root2.left):
                return False
            if not self.isSameTree(root1.right, root2.right):
                return False
            return True

node1 = Node(5)
node1.left = Node(3)

node2 = Node(5)
node2.left = Node(2)

s = Solution()
print (s.isSameTree(node1, node2))