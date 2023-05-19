from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        node, other = head, _ = (list1, list2) if list1.val <= list2.val else (list2, list1)
        while node and other:
            while node.next and node.next.val <= other.val: node = node.next
            node.next, _ = node, other = other, node.next
        return head


l1 = ListNode(-9)
l1.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(7)
test = Solution()
x = test.mergeTwoLists(l1, l2)
print(10)
