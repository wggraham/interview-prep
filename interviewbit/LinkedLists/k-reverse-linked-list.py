# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, root, k):
        def revList(cur):
            if not cur: return
            prev = None
            for _ in range(k-1):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            if cur:
                root.next = revList(cur)

            return prev

        return revList(root)

    def reverseList2(self, A, B):
        if B == 1: return A

        prior, prev, cur = None, None, A
        while cur:
            head, prev, nxt, k = cur, None, cur.next, B

            while cur and k > 1:
                cur.next = prev
                prev = cur
                cur = nxt
                nxt = nxt.next if nxt else None
                k -= 1

            head.next = cur.next
            cur.next = prev
            if prev:
                prev.next = cur
            else:
                prior = cur

            cur = head.next
        return prior

    def reverseList3(self, A, B):
        if B == 1:
            return A
        prior = None
        prev, cur = None, A
        while cur:
            k = B
            head = cur
            p, n = None, cur.next

            while cur and k > 1:
                cur.next = p
                p = cur
                cur = n
                n = n.next if n else None
                k -= 1
            head.next = cur.next
            cur.next = p
            if prev:
                prev.next = cur
            else:
                prior = cur
            prev = head
            cur = head.next
        return prior

    def reverseList4(self, A, B):
        prev = None
        cur = A
        nxt = None
        c = 0
        while cur and c < B:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            c += 1
        if nxt:
            A.next = Solution.reverseList(self, nxt, B)
        return prev


root = ListNode(3)
root.next = ListNode(4)
root.next.next = ListNode(7)
root.next.next.next = ListNode(5)
root.next.next.next.next = ListNode(6)
root.next.next.next.next.next = ListNode(6)
root.next.next.next.next.next.next = ListNode(15)
root.next.next.next.next.next.next.next = ListNode(61)
root.next.next.next.next.next.next.next.next = ListNode(16)
test = Solution()
x = test.reverseList4(root, 2)
x = test.reverseList(root, 2)
print(10)
