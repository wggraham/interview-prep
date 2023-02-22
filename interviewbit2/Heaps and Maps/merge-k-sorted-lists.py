import time
from heapq import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, A):
        head = node = ListNode(0)
        h = [(node.val, node) for node in A]
        heapify(h)

        while h:
            node.next = node = heappop(h)[1]
            if not node.next: continue
            heappush(h, (node.next.val, node.next))

        return head.next

    def mergeKLists2(self, A):
        head = node = ListNode(0)
        h = [(node.val, node) for node in A]
        heapify(h)

        while h:
            _, nxt = heappop(h)
            node.next = nxt
            node = nxt
            if node.next:
                heappush(h, (node.next.val, node.next))

        return head.next


a = ListNode(1)
a.next = ListNode(10)
a.next.next = ListNode(20)
b = ListNode(4)
b.next = ListNode(11)
b.next.next = ListNode(13)
c = ListNode(3)
c.next = ListNode(8)
c.next.next = ListNode(9)
t = [a, b, c]
test = Solution()
t1 = time.time()
x = test.mergeKLists(t)
t2= time.time()

print(t2-t1)
