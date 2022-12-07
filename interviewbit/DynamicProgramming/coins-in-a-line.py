class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        if len(A) < 3:
            return max(A)
        s = []
        for val in A:
            s.append(val)
            while len(s) > 2:
                y, m, x = s.pop(), s.pop(), s.pop()

                if x <= m and y <= m:
                    s.append(x - m + y)
                else:
                    s.append(x)
                    s.append(m)
                    s.append(y)
                    break
        return s


A = [5, 8, 4, 10]
A = [1, 2, 3, 4]
test = Solution()
print(test.maxcoin(A))
