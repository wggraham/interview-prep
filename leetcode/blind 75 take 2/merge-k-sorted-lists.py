from queue import PriorityQueue
from typing import List, Optional
from heapq import heappop, heappush, heapify


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda s, other: s.val <= other.val)

        h = []

        for i in range(len(lists)):
            heappush(h, lists[i])

        head = node = heappop(h)
        if node.next:
            heappush(h, node.next)
        node.next = h[0]

        while h:
            node = heappop(h)

            if node.next:
                heappush(h, node.next)
            if h:
                node.next = h[0]
        return head

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda s, other: s.val <= other.val)
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

    def mergeKLists4(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda s, other: s.val <= other.val)
        head = node = ListNode()

        h = [(n.val, n) for n in lists]
        while h:
            _, n = heappop(h)
            node.next = n
            node = node.next
            if n.next:
                heappush(h, (n.next.val, n.next))

        return head.next


node = ListNode(1)
node.next = ListNode(4)
node.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

test = Solution()
#x = test.mergeKLists([node, node2, node3])
x = test.mergeKLists4([node, node2, node3])

l = []
while x:
    l.append(x.val)
    x = x.next

print(l)
