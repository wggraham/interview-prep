from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        counts = Counter(s)
        n = len(counts)
        total = 0
        m = 0
        st = set()
        for c in s:
            counts[c] -= 1
            if not counts[c]:
                n -= 1
            if c not in st:
                m += 1
                st.add(c)
            if n == m:
                total += 1
        return total



s = "aacaba"
test = Solution()
print(test.numSplits(s))
