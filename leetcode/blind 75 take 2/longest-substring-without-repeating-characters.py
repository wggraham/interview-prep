class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, j = 0, 0
        st = set()
        for i, c in enumerate(s):
            if c in st:
                while s[j] != c:
                    st.remove(s[j])
                    j += 1
                j += 1
            st.add(c)
            longest = max(longest, i - j + 1)
        return longest


test = Solution()
s = "au"
s = "abcabcbb"
s = " "
print(test.lengthOfLongestSubstring(s))
