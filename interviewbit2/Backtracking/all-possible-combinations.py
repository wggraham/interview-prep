class Solution:
    def specialStrings(self, A):
        res = ['']

        for s in A:
            res = [p + c for p in res for c in s]

        return res


A = [ "ozqz", "p", "abm" ]

test = Solution()
print(test.specialStrings(A))







