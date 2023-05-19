from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def isLengthK(node):
            for _ in range(k):
                if not node:
                    return False
                node = node.next
            return True

        def revk(cur):
            root = prev = ListNode(next=cur)
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            root.next.next = cur
            return prev, root.next

        root = prev = ListNode(next=head)
        node = head
        while isLengthK(node):
            prev.next, tail = revk(node)
            node = tail.next
            prev = tail

        return root.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
# root.next.next.next.next.next = ListNode(6)
# root.next.next.next.next.next.next = ListNode(7)

k = 3
test = Solution()
x = test.reverseKGroup(root, k)
print(10)
