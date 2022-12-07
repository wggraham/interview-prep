class Solution:
    def solve(self, A, B):
        chars, count, prev = [], 1, A[0]
        for c in A[1:] + '0':
            if c != prev:
                chars.append((prev, count))
                count = 0
            prev = c
            count += 1

        res = []
        for c, count in chars:
            res += [c] * count if count != B else []
        return ''.join(res)



A = "aabcd"
B = 2
A = "aabbccd"
B = 2
test = Solution()
print(test.solve(A, B))
