class Solution:
	def combinationSum(self, A, B):
		if not A: return 0

		def countCombo(a, p, t):
			if t < 0: return
			if t == 0: return [p]
			res = []
			for v in a:
				y = t
				temp = []
				while y >= 0:
					y -= v
					temp.append(v)
				while temp:
					x = countCombo(a[1:], p + temp, y)
					if x:
						res.extend(x)
					temp.pop()
					y += v
			return res

		A = set(A)
		A = sorted(list(A))
		return countCombo(A, [], B)

A = [2,3]
B = 2
# A = [2, 3, 6, 7]
# B = 7
A = [ 8, 10, 6, 11, 1, 16, 8 ]
B = 28

test = Solution()
print(test.combinationSum(A, B))
