# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        odd = head
        eHead = even = head.next
        cur = head.next.next
        e = False

        while cur:
            if e:
                even.next = even = cur
            else:
                odd.next = odd = cur
            cur = cur.next
            e = not e
        odd.next = eHead
        even.next = None
        return head



test = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
b = test.oddEvenList(a)
print(10)
