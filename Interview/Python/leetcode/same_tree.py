class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

t1=TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)

t2=TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)

t3=TreeNode(1)
t3.left = TreeNode(2)
t3.right = TreeNode(5)

t4=TreeNode(1)
t4.left = TreeNode(2)


def is_same_tree(t1, t2):
    if t1 is None or t2 is None:
        if t1 is None and t2 is None:
            return True
        else:
            return False

    if t1.val != t2.val:
        return False

    if not is_same_tree(t1.left, t2.left):
        return False

    if not is_same_tree(t1.right, t2.right):
        return False

    return True

print (is_same_tree(t1, t2))
print (is_same_tree(t1, t3))
print (is_same_tree(t1, t4))

st1 = str(t1)
st2 = str(t2)
print(str(t1))
print (str(t2))
print(st1==st2)