from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = head = ListNode()
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node.next = ListNode((v1 + v2 + carry) % 10)
            carry = (v1 + v2 + carry) // 10
            node = node.next
        if carry:
            node.next = ListNode(carry)
        return head.next


def genNodes(l):
    node = head = ListNode()
    for v in l:
        node.next = ListNode(v)
        node = node.next
    return head.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

l1 = genNodes(l1)
l2 = genNodes(l2)
test = Solution()
res = test.addTwoNumbers(l1, l2)
l = []
while res:
    l += [res.val]
    res = res.next

print(l)
