class Solution:
	# @param A : integer
	# @return a strings
	def countAndSay(self, A):
		if A <= 0: return "0"

		def get_next():
			nonlocal res
			i, n = 1, len(res)
			res += [0]
			temp = []
			count = 1
			while i <= n:
				if res[i] != res[i-1]:
					temp += [count] + [res[i-1]]
					count = 0
				count += 1
				i += 1
			return temp

		res = [1]
		for i in range(1, A):
			res = get_next()
		return ''.join(str(x) for x in res)


n = 6
test = Solution()
print(test.countAndSay(n))
