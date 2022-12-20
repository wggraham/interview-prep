# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def solve(self, A, B):
        head = ListNode(0)
        head.next = A

        rev, cur, prior, prev, i = True, A, head, head, 0
        while cur:
            if rev:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            else:
                prev = cur
                cur = cur.next

            i += 1
            if i % B:
                continue
            rev = not rev
            if rev:
                prior = prev
                continue
            temp = prior.next
            prior.next = prev
            prior = temp
            prior.next = cur

        return head.next

    def kAltReverse(self, head, k):
        if not head: return
        current, prev, count = head, None, 0

        while current and count < k:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            count += 1

        head.next = current
        count = 0
        while current and count < k - 1:
            current = current.next
            count += 1

        if not current:
            return prev

        current.next = self.kAltReverse(current.next, k)

        return prev  # prev is new head of the input list


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
x = test.solve(root, 3)
print(10)
