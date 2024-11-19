lass TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

def get_diameter(root):
    if root is Null:
        return 0
    return 1 + max (get_diameter(root.left), get_diameter(root.right))
