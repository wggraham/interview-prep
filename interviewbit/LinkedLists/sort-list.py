# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def merge(a, b):
	root = a if a.val <= b.val else b
	s, e = (a, b) if a.val < b.val else (b, a)
	while s and e:
		if s and e and s.val <= e.val:
			if (s.next and s.next.val > e.val) or (not s.next and e):
				temp = s.next
				s.next = e
				e = temp
			s = s.next
		if s and e and s.val > e.val:
			if (e.next and e.next.val < s.val) or (not e.next and s):
				temp = e.next
				e.next = s
				s = temp
			e = e.next
	return root


class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
		if A is None or A.next is None: return A
		i, n = A, 0
		while i:
			i = i.next
			n += 1

		def mergeSort(s, n):
			if n < 3: return s
			m = n // 2
			p = s

			for _ in range(m-1):
				p = p.next
			t = p.next
			p.next = None
			return merge(mergeSort(s, m), mergeSort(t, n - m))

		return mergeSort(A, n)

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