from typing import List, Optional
from heapq import heapify, heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(node.val, i, node) for i, node in enumerate(lists)]
        heapify(h)
        _, i, node = heappop(h)
        if node.next:
            heappush(h, (node.next.val, i, node.next))

        root = node
        while h:
            _, i, node.next = heappop(h)
            node = node.next
            if node.next:
                heappush(h, (node.next.val, i, node.next))

        return root


a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
c = ListNode(2)
c.next = ListNode(6)

test = Solution()
print(test.mergeKLists([a,b,c]))
