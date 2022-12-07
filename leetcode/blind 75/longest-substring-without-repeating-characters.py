class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        st = set()
        j = 0

        for i, v in enumerate(s):
            if v in st:
                longest = max(longest, i - j)
                while st and s[j] != v:
                    st.remove(s[j])
                    j += 1
                st.remove(s[j])
                j += 1

            st.add(v)
        return max(longest, len(s) - j)


s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
test = Solution()
print(test.lengthOfLongestSubstring(s))
