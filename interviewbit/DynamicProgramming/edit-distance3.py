class Solution:
    def minDistance(self, A, B):
        A, B = B, A if len(B) > len(A) else [A, B]
        dp = [0] + [i+1 for i in range(len(B))]

        for i in range(len(A)):
            tmp = copy(dp)
            for j in range(len(B)):
                if A[i] == B[j]:
                    tmp[j+1] = dp[j]
                else:
                    tmp[j+1] = min(dp[j], dp[j+1], tmp[j]) + 1
            dp = tmp
        return dp[-1]

# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def minDistance(self, A, B):
#         A = '0' + A
#         B = '0' + B
#
#         r = [[0 for i in range(len(A))] for j in range(len(B))]
#
#         for i in range(1, len(A)):
#             r[0][i] = i
#
#         for i in range(1, len(B)):
#             r[i][0] = i
#
#         for i in range(1, len(B)):
#             for j in range(1, len(A)):
#                 if A[j] == B[i]:
#                     r[i][j] = r[i-1][j-1]
#                 else:
#                     r[i][j] = min(r[i-1][j-1],
#                                   r[i][j-1],
#                                   r[i-1][j],
#                                   ) + 1
#
#         return r[-1][-1]

a = "aaa"
b = "aa"
# a = "Anshuman"
# b = "Antihuman"
test = Solution()
print(test.minDistance(a, b))
