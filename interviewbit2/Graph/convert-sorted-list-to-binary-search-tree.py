# Definition for a  binary tree node
from math import ceil


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        def buildTree(front, n):
            if n < 1: return
            if n < 2:
                return TreeNode(front.val) if front else None
            m = n // 2 if n % 2 else ceil(n / 2)
            node = front
            for _ in range(m - 1):
                node = node.next
            root = TreeNode(node.next.val)
            root.left = buildTree(front, m)
            root.right = buildTree(node.next.next, m)
            return root

        n, node = 0, A
        while node:
            n += 1
            node = node.next

        return buildTree(A, n)

    def sortedListToBST2(self, head):
        if not head: return

        def bst(node, st, ed):
            if st > ed or not node[0]:
                return
            mid = (st + ed) // 2
            left = bst(node, st, mid - 1)
            root = TreeNode(node[0].val)
            node[0] = node[0].next
            right = bst(node, mid + 1, ed)
            root.left = left
            root.right = right
            return root

        n, tmp = 0, head
        while tmp:
            n += 1
            tmp = tmp.next
        return bst([head], 0, n)


A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
A.next.next.next = ListNode(4)
A.next.next.next.next = ListNode(5)
test = Solution()
x = test.sortedListToBST2(A)
print(10)
