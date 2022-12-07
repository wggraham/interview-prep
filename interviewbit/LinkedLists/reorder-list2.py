class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, A):
        def reverseList(node):
            prev = node
            cur = node.next
            prev.next = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        def interleave(front, back):
            while back.next:
                temp = front.next
                front.next = back
                back = back.next
                front.next.next = temp
                front = temp
        if not A.next:
            return A
        fast, slow = A, A
        while fast and fast.next:
            fast = fast.next.next if fast.next else fast.next
            slow = slow.next

        interleave(A, reverseList(slow))
        return A


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)
# root.next.next.next.next.next.next = ListNode(7)
test = Solution()
x = test.reorderList(root)

while x:
    print(x.val)
    x = x.next
