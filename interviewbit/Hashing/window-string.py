from collections import Counter

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        counts = Counter(B)
        found = False
        s = set(B)
        minW = len(A)
        minWindow = window = (0, len(A))
        i = 0
        while i < len(A) and A[i] not in counts:
            i += 1

        j = i
        while i < len(A):
            if A[i] in counts:
                counts[A[i]] -= 1
                if counts[A[i]] == 0:
                    s.remove(A[i])
            i += 1
            while j < i and len(s) == 0:
                found = True
                if A[j] in counts:
                    if counts[A[j]] == 0:
                        window = (j, i)
                        counts[A[j]] += 1
                        s.add(A[j])
                    if counts[A[j]] < 0:
                        counts[A[j]] += 1
                j += 1

            if window[1] - window[0] < minW:
                minW = window[1] - window[0]
                minWindow = window


        return A[minWindow[0]:minWindow[1]] if found else ""


A = "z3OyxTp7j3usoz2l0zmr8tJCocoNUvL1cVTWuroYKTluh60TsRvR8jNjiStkt2FNRxPtUn4ZTWSeqgClbFyPWqUHTaSRC5cY5JPVAW25IGusbMaRYmPWUOswP0QnU1BFYldSoDEV59efpkUXI6BQ6vnTAB4"
B = "m"
test = Solution()
print(test.minWindow(A, B))

S = "ADOBECODEBANCABC"
T = "ABC"
print(test.minWindow(S, T))
