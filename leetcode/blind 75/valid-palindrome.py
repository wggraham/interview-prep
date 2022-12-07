import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lc = set(string.ascii_lowercase + string.digits)
        chars = [c for c in s.lower() if c in lc]

        i, j = 0, len(chars) - 1
        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1
        return True



s = "A man, a plan, a canal: Panama"
test = Solution()
print(test.isPalindrome(s))
