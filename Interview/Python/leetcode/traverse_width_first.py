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

def width_first_traverse(root):
    # Create a queue to hold the nodes to be processed
    queue = [root]

    # Loop until the queue is empty
    while queue:
        # Get the next node to be processed
        node = queue.pop(0)

        # Process the node (e.g., print it)
        print(node.val)

        # Add the children of the node to the queue, if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


width_first_traverse(four)