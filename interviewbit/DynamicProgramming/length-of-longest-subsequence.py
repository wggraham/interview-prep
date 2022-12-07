class Solution:
    def longestSubsequenceLength(self, A):
        incSub = self.getLongestSubSeqAllPositions(A)
        decSub = self.getLongestSubSeqAllPositions(A[::-1])[::-1]
        maxLen = 0

        for i in range(len(A)):
            maxLen = max(maxLen, incSub[i] + decSub[i] - 1)
        return maxLen

    def getLongestSubSeqAllPositions(self, seq):
        z = [0]
        lisLenAt = [1] * len(seq)

        for i, val in enumerate(seq):
            j = self.binSearch(seq, z, val)
            if j == len(z):
                z.append(i)
            z[j] = i            # index of min endVal for subseq of length j
            lisLenAt[i] = max(lisLenAt[i-1], j + 1)
        return lisLenAt

    def binSearch(self, seq, z, val):
        if val <= seq[z[0]]:    # check if value is smallest seen so far
            return 0
        if val > seq[z[-1]]:
            return len(z)       # check if value is largest seen so far

        s, e = 0, len(z) - 1
        while s < e:
            m = (s + e) // 2
            curVal = seq[z[m]]
            s, e = (s, m) if val <= curVal else (m + 1, e)

        return m + 1 if m < len(z) - 1 and seq[z[m]] < val <= seq[z[m + 1]] else m


t = [1, 11, 2, 10, 4, 5, 2, 1, 6]
t = [1, 11, 2, 10, 4, 5, 2, 1]
test = Solution()
print(test.longestSubsequenceLength(t))
