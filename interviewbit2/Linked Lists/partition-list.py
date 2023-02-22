# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, A, B):
        less, more, node = [], [], A
        while node:
            if node.val < B:
                less.append(node.val)
            else:
                more.append(node.val)

            node = node.next

        node = A
        for val in less + more:
            node.val = val
            node = node.next

        return A

    # in-place
    # def partition2(self, A, B):
    #     pivot_count = 0
    #     node = A
    #     while node:
    #         if node.val < B:
    #             pivot_count += 1
    #         node = node.next
    #
    #     node = A
    #     count, pre_pivot_count, post_pivot_count = pivot_count, 0, 0
    #     while node:
    #         count -= 1
    #         node = node.next
    #         pre_pivot_count += 1 if node.val <= B and count > 0 else 0
    #         post_pivot_count += 1 if node.val <= B and count <= 0 else 0
    #
    #
    #     return A

    # can do this much more simply by just swapping front and back
    def partition3(self, head, x):
        if not head: return

        front, back, node = ListNode(0), ListNode(0), head
        head, pivot = front, back
        while node:
            if node.val < x:
                front.next = front = node
            else:
                back.next = back = node

            tmp = node
            node = node.next
            tmp.next = None

        front.next = pivot.next
        return head.next


root = ListNode(3)
root.next = ListNode(3)
root.next.next = ListNode(7)
root.next.next.next = ListNode(7)
root.next.next.next.next = ListNode(6)
root.next.next.next.next.next = ListNode(6)
root.next.next.next.next.next.next = ListNode(5)
root.next.next.next.next.next.next.next = ListNode(9)
root.next.next.next.next.next.next.next.next = ListNode(16)
test = Solution()
x = test.partition3(root, 6)
print(10)
