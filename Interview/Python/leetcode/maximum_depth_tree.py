class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


def get_max_depth_rec(root):
    if root is None:
        return 0
    return 1 + max(get_max_depth_rec(root.left), get_max_depth_rec(root.right))

print (get_max_depth_rec(root))


#def get_max_depth_iter(root):
