from sys import maxsize


class Solution:
    def majorityElement(self, A):
        if not A or not len(A):
            return 0
        if len(A) < 2:
            return A[0]

        m = [maxsize, 1]

        for val in A:
            if val == m[0]:
                m[1] += 1
            else:
                m[1] -= 1
            if m[1] == 0:
                m[0], m[1] = val, 1
        return m[0]


test = Solution()
a = [1, 2, 2, 3, 1, 3, 2]
#a = [ 1, 1, 1, 2, 2 ]
print(test.majorityElement(a))
