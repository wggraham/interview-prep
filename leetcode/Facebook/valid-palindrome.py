import re
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        return s == s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        return s == s[::-1]

    def isPalindrome3(self, s: str) -> bool:
        chars = set(string.digits + string.ascii_lowercase)
        s = [c for c in s.lower() if c in chars]
        return s == s[::-1]


s = "A man, a plan, a canal: Panama"
# s = "0P"
test = Solution()
print(test.isPalindrome(s))
print(test.isPalindrome2(s))
print(test.isPalindrome3(s))
