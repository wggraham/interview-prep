from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        m = defaultdict(list)

        for i, v1 in enumerate(A):
            for j, v2 in enumerate(A[i+1:]):
                m[v1 + v2].append((i, j+i+1))

        for i, v1 in enumerate(A):
            for j, v2 in enumerate(A[i+1:]):
                if (v1 + v2) in m and len(m[v1+v2]) > 1:
                    s = set(m[v1+v2][0])
                    k = 1
                    while k < len(m[v1+v2]):
                        x, y = m[v1+v2][k]
                        if x not in s and y not in s:
                            return [m[v1 + v2][0][0], m[v1 + v2][0][1], x, y]
                        k += 1

        return


a = [ 1, 1, 1, 1, 1 ]
test = Solution()
print(test.equal(a))
