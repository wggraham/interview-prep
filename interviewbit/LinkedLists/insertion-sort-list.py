class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, A):
        def swap(node1, node2):
            node1.val, node2.val = node2.val, node1.val

        def get_min(node):
            min_node = node
            while node:
                min_node = node if node.val < min_node.val else min_node
                node = node.next
            return min_node

        node = A
        while node:
            min_node = get_min(node)
            swap(node, min_node)
            node = node.next
        return A