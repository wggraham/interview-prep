# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, node):
        prev, cur = None, node
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def mergeLists(self, front, back):
        while front.next and back:
            fn = front.next
            bn = back.next
            front.next = back
            back.next = fn
            front = fn
            back = bn
        front.next = None

    def reorderList(self, A):
        if not A or not A.next or not A.next.next:
            return A
        slow, fast = A, A

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        self.mergeLists(A, self.reverseList(slow))
        return A



def convertToList(s):
    s = s.split("[")
    s = s[1].split("]")
    s = s[0].split("->")
    nums = [int(x) for x in s]
    node = root = ListNode(nums[0])
    for v in nums[1:]:
        node.next = ListNode(v)
        node = node.next

    return root

root = ListNode(1)
# root.next = ListNode(2)
# root.next.next = ListNode(3)
# root.next.next.next = ListNode(4)


s = "[ 90 -> 94 -> 25 -> 51 -> 45 -> 29 -> 55 -> 63 -> 48 -> 27 -> 72 -> 10 -> 36 -> 68 -> 16 -> 20 -> 31 -> 7 -> 95 -> 70 -> 89 -> 23 -> 22 -> 9 -> 74 -> 71 -> 35 -> 5 -> 80 -> 11 -> 49 -> 92 -> 69 -> 6 -> 37 -> 84 -> 78 -> 28 -> 43 -> 64 -> 96 -> 57 -> 83 -> 13 -> 73 -> 97 -> 75 -> 59 -> 53 -> 52 -> 19 -> 18 -> 98 -> 12 -> 81 -> 24 -> 15 -> 60 -> 79 -> 34 -> 1 -> 54 -> 93 -> 65 -> 44 -> 4 -> 87 -> 14 -> 67 -> 26 -> 30 -> 77 -> 58 -> 85 -> 33 -> 21 -> 46 -> 82 -> 76 -> 88 -> 66 -> 101 -> 61 -> 47 -> 8 ]"
s = "[ 12 -> 6 -> 75 -> 98 -> 58 -> 81 -> 30 -> 101 -> 87 -> 40 -> 70 -> 45 -> 41 -> 20 -> 66 -> 1 -> 96 -> 35 -> 51 -> 79 -> 61 -> 48 -> 99 -> 11 -> 32 -> 88 -> 60 -> 18 -> 42 -> 29 -> 13 -> 91 -> 85 -> 10 -> 33 -> 52 -> 84 -> 4 -> 94 -> 46 -> 23 -> 82 -> 59 -> 38 -> 97 -> 17 -> 14 -> 90 -> 54 -> 69 -> 57 -> 74 -> 73 -> 39 ]"
root = convertToList(s)

test = Solution()
x = test.reorderList(root)
while x:
    print(x.val)
    x = x.next

