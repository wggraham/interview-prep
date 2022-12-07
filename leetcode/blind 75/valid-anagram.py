from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2


s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
test = Solution()
print(test.isAnagram(s, t))
