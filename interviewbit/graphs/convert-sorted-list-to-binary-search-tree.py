# Definition for a  binary tree node
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
    def sortedListToBST(self, head):
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        def buildTree(i, j):
            if i > j: return
            m = (i + j) // 2
            node = TreeNode(nums[m])
            node.left = buildTree(i, m - 1)
            node.right = buildTree(m + 1, j)
            return node

        return buildTree(0, len(nums)-1)

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
test = Solution()
x = test.sortedListToBST(root)
print(10)