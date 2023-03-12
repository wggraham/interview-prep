class Solution:
    def lengthOfLastWord(self, A):
        i = len(A) - 1
        while i >= 0 and A[i] == ' ':
            i -= 1
        j = i
        while j >= 0 and A[j] != ' ':
            j -= 1
        return i - j if i >= 0 else 0


A = " hello world "
test = Solution()
print(test.lengthOfLastWord(A))
