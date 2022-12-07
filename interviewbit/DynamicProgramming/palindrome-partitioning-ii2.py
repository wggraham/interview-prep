from time import *


class Solution:
	def minCut(self, A):
		if not A:
			return 0

		minCuts = [len(A)] * (len(A) + 1)
		minCuts[0] = -1
		n = len(minCuts)

		for i in range(1, n):
			for j in range(i):
				if not A[j:i] == A[j:i][::-1]:		# is A[j:i] substring a palindrome
					continue
				minCuts[i] = min(minCuts[i], minCuts[j] + 1)

		return minCuts[-1]

	def minCut2(self, A):
		if not A:
			return 0

		minCuts = [len(A)] * (len(A) + 1)
		minCuts[0] = -1
		n = len(minCuts)

		def isPal(s):
			return s == s[::-1]

		for i in range(1, n):
			for j in range(i):
				if not isPal(A[j:i]):		# is A[j:i] substring a palindrome
					continue
				minCuts[i] = min(minCuts[i], minCuts[j] + 1)

		return minCuts[-1]

s = "abccbadlk;jasjlk;boeeonasdeoxhanbanadalsdoea"
test = Solution()
t0 = time()
test.minCut2(s)
t1 = time()
test.minCut(s)
t2 = time()
print(t1 - t0)
print(t2 - t1)