from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        frequencies = counts.most_common(len(counts))
        n_max = 0
        for n_max, freq in enumerate(frequencies, 1):
            if freq[1] != frequencies[0][1]:
                n_max -= 1
                break
        return max(len(tasks), (frequencies[0][1] - 1) * (n + 1) + n_max)

tasks = ["A","A","A","B","B","B"]
n = 2
# tasks = ["A","A","A","B","B","B"]
# n = 0
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
test = Solution()
print(test.leastInterval(tasks,n))