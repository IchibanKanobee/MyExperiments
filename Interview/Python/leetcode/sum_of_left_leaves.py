class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


four = TreeNode(4)
four.left = TreeNode(2)
four.right = TreeNode(7)
four.left.left = TreeNode(1)
four.left.right = TreeNode(3)
four.right.left = TreeNode(6)
four.right.right = TreeNode(9)


def get_sum_of_left_leaves(node, sum):
    if node is None:
        return sum
    if node.val is None:
        return sum
    if node.left is not None:
        sum += node.left.val
    sum = get_sum_of_left_leaves(node.left, sum)
    sum = get_sum_of_left_leaves(node.right, sum)
    return sum

print(get_sum_of_left_leaves(four, 0))
