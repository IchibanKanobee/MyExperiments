class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



class Solution:
    # def removeElements(self, node, val):
    #     previousNode = Node(-1)
    #     if node.val != val:
    #         previousNode.next = node

   def removeElements(self, head, val):
        dummy=Node(-1)
        dummy.next=head
        curr=dummy
        while curr.next is not None:
            if curr.next.val==val:
                curr.next=curr.next.next
                #curr=curr.next
            else:
                curr=curr.next
        return dummy.next



node = Node(1)
node.next = Node(2)
node.next.next = Node(6)
node.next.next.next = Node(3)
node.next.next.next.next = Node(4)
node.next.next.next.next.next = Node(5)
node.next.next.next.next.next.next = Node(6)

s = Solution()
newList = s.removeElements(node, 6)
print(newList)
