from sys import maxsize


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestSubsequenceLength(self, A):
		dp = defaultdict(list)

		l = -maxsize
		for i, v in enumerate(A):
			if v < l:
				l = v






A = [1, 11, 2, 10, 4, 5, 2, 1]
test = Solution()
print(test.longestSubsequenceLength(A))
