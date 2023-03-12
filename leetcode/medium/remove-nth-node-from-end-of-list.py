from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for i in range(n): fast = fast.next
        if not fast: return slow.next
        while fast: slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return head


head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
test = Solution()
x = test.removeNthFromEnd(head, 2)
print(10)
