class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def solve(self, A, B):
        n = 0
        node = A
        while node:
            node = node.next
            n += 1

        m = n // 2
        node = A
        for _ in range(m - B):
            node = node.next

        return node.val if m >= B else -1


