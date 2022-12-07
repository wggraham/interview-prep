class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def solve(self, A):
        node, count = A, 0
        while node:
            count += 1 if node.val == 0 else 0
            node = node.next

        node = A
        while node:
            node.val = 0 if count else 1
            count -= 1 if count else 0

        return A



