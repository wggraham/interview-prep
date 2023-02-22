
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, A):
        node, s = A, []
        while node:
            v = node
            while node and node.val == v.val:
                node = node.next

            if node == v.next:
                s.append(v.val)

        if not s:
            return
        node = A
        for val in s[:-1]:
            node.val = val
            node = node.next
        node.val = s[-1]
        node.next = None
        return A

    def deleteDuplicates2(self, node):
        head = prev = ListNode(0)
        while node and node.next:
            if node.val != node.next.val:
                prev = prev.next
                node = node.next
                continue

            while node.next and node.val == node.next.val:
                node = node.next
            prev.next = node.next
            node = node.next

        return head.next


root = ListNode(3)
root.next = ListNode(3)
root.next.next = ListNode(7)
root.next.next.next = ListNode(7)
root.next.next.next.next = ListNode(6)
root.next.next.next.next.next = ListNode(6)
root.next.next.next.next.next.next = ListNode(5)
root.next.next.next.next.next.next.next = ListNode(9)
# root.next.next.next.next.next.next.next.next = ListNode(16)
test = Solution()
x = test.deleteDuplicates2(root)
print(10)
