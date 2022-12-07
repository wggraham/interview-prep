from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
