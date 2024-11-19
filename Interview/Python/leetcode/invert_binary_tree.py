# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return root

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root

four = TreeNode(4)
four.left = TreeNode(2)
four.right = TreeNode(7)
four.left.left = TreeNode(1)
four.left.right = TreeNode(3)
four.right.left = TreeNode(6)
four.right.right = TreeNode(9)

def print_tree(node):
    if node is None:
        return
    if node.val != None:
        print(node.val)
    print_tree(node.left)
    print_tree(node.right)

def reverse_tree(node):
    if node is None:
        return None
    node_left = node.left
    node_right = node.right
    node.left = node_right
    node.right = node_left
    reverse_tree(node_left)
    reverse_tree(node.right)

print_tree(four)
reverse_tree(four)
print("---------------------------")
reverse_tree(four)
print_tree(four)