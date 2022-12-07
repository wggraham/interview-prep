from collections import deque


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def t2Sum(self, root, target):

        sums = set()
        q = deque([root])
        while q:
            node = q.pop()
            if target - node.val in sums:
                return 1
            sums.add(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return 0

    def t2Sum2(self, root, target):
        node, arr, stack = root, [], []
        while node:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                arr.append(node.val)
                node = node.right

        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] + arr[j] == target:
                return 1
            elif arr[i] + arr[j] > target:
                j -= 1
            else:
                i += 1
        return 0
