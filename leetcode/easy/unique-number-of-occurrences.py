from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr).values()
        s = set(count)
        return len(count) == len(s)
