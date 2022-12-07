from collections import Counter


class Solution:
    def majorityElement(self, A):
        counts = Counter(A)
        return counts.most_common(1)[0][0]

    def majorityElement2(self, A):
        counts = Counter(A)
        uniques = set(A)

        m = 0
        mv = None
        for v in uniques:
            if counts[v] > m:
                m = counts[v]
                mv = v
        return mv
