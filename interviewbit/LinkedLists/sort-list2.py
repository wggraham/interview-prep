class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(left, right):
    left, right = (right, left) if left.val > right.val else (left, right)
    root = node = left
    left = left.next
    while True:
        if not left or not right:
            node.next = left if left else right
            break
        if left.val <= right.val:
            node.next = left
            left = left.next
        else:
            node.next = right
            right = right.next
        node = node.next
    return root


class Solution:
    def sortList(self, A):
        def mergeSort(s):
            if not s or not s.next:
                return s

            if not s.next.next:
                t = s.next
                s.next = None
                return merge(s, t)

            fast, slow = s, s
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            mid = slow.next
            slow.next = None
            return merge(mergeSort(s), mergeSort(mid))

        if A is None or A.next is None:
            return A
        return mergeSort(A)


def toList(a):
    root = ListNode(a[0])
    node = root
    for v in a[1:]:
        node.next = ListNode(v)
        node = node.next
    return root


A = "5 -> 66 -> 68 -> 42 -> 73 -> 25 -> 84 -> 63 -> 72 -> 20 -> 77 -> 38 -> 8 -> 99 -> 92 -> 49 -> 74 -> 45 -> 30 -> 51 -> 50 -> 95 -> 56 -> 19 -> 31 -> 26 -> 98 -> 67 -> 100 -> 2 -> 24 -> 6 -> 37 -> 69 -> 11 -> 16 -> 61 -> 23 -> 78 -> 27 -> 64 -> 87 -> 3 -> 85 -> 55 -> 22 -> 33 -> 62"
A = A.split(' -> ')
A = [int(x) for x in A]
test = Solution()
x = test.sortList(toList(A))
print(10)
