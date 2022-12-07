from heapq import heapify, heappop, heappush, heapreplace
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        h = [(n.val, n) for n in A]
        heapify(h)
        node = root = ListNode(None)

        while h:
            node.next = node = heappop(h)[1]
            if node.next:
                heappush(h, (node.next.val, node.next))

        return root.next

    def mergeKLists2(self, A):
        h = [(n.val, n) for n in A]
        heapify(h)
        node = root = ListNode(None)
        node.next = node = heapreplace(h, (h[0][1].next.val, h[0][1].next))[1]
        while h:
            while h[0][1].next:
                node.next = node = heapreplace(h, (h[0][1].next.val, h[0][1].next))[1]
            node.next = node = heappop(h)[1]

        return root.next


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
a = ListNode(1)
a.next = ListNode(10)
a.next.next = ListNode(20)
b = ListNode(4)
b.next = ListNode(11)
b.next.next = ListNode(13)
c = ListNode(3)
c.next = ListNode(8)
c.next.next = ListNode(9)
z = [a, b, c]
t3= time.time()
y = test.mergeKLists2(z)
t4= time.time()
print(t2-t1)
print(t4-t3)
