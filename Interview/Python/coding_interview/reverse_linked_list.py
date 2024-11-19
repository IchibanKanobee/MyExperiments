class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, node):
        stack = []
        currentNode = node
        while not currentNode is None:
            stack.append(currentNode)
            currentNode = currentNode.next

        newRoot = ListNode(stack.pop().val)
        newCurrentNode = newRoot
        while len(stack) > 0:
            newCurrentNode.next = ListNode(stack.pop().val)
            newCurrentNode = newCurrentNode.next

        return newRoot

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)

s = Solution()

newRoot = s.reverseList(node)
print(newRoot)


