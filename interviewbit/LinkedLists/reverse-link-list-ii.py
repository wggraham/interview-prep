# Definition for singly-linked list.
import pickle


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reverseBetween(self, head, m, n):
		if m == n: return head
		root = head
		if m == 1:
			root = ListNode(0)
			root.next = head
			m += 1
			n += 1

		node = root
		for _ in range(m-2):
			node = node.next

		pm = node
		prev = node.next
		cur = node.next.next
		for _ in range(n - m-1):
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt

		prev.next = cur.next
		cur.next = prev
		pm.next = cur

		return head if root != head else pm.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
test = Solution()
print(test.reverseBetween(head, 2, 3))
