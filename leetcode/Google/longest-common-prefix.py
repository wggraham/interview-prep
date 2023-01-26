from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        n = min(len(word) for word in strs)
        for i in range(n):
            c = strs[0][i]
            for word in strs:
                if word[i] != c:
                    return strs[0][:count] if count else ""
            count += 1

        return strs[0][:count]


strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
test = Solution()
print(test.longestCommonPrefix(strs))
