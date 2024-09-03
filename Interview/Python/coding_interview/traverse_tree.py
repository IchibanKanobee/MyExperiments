class Node:
    def __init__(self, key):
        self.key = key,
        self.left = None
        self.right = None



def traverse_tree_inorder(node):
    if not node.left is None:
        traverse_tree_inorder(node.left)
    print(node.key)
    if not node.right is None:
        traverse_tree_inorder(node.right)

def traverse_tree_preorder(node):
    print(node.key)
    if not node.left is None:
        traverse_tree_preorder(node.left)
    if not node.right is None:
        traverse_tree_preorder(node.right)


def traverse_tree_postorder(node):
    if not node.left is None:
        traverse_tree_postorder(node.left)
    if not node.right is None:
        traverse_tree_postorder(node.right)
    print(node.key)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

traverse_tree_inorder(root)
print("-----------------------------------")
traverse_tree_preorder(root)
print("-----------------------------------")
traverse_tree_postorder(root)
print("-----------------------------------")
