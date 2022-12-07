class Solution:
    def longest_palindrome(self, s: str) -> str:
        #t = '^' + '#' + '#'.join(list(s)) + '#' + '$'
        t = '$' + '#' + '#'.join(list(s)) + '#' + '^'
        n = len(t)
        palindrome_length_at_index = [0] * n
        c = r = 0

        for i in range(1, n - 1):
            # initialize palindrome length to
            palindrome_length_at_index[i] = max(0, min(r - i, palindrome_length_at_index[2 * c - i]))

            while t[i + 1 + palindrome_length_at_index[i]] == t[i - 1 - palindrome_length_at_index[i]]:
                palindrome_length_at_index[i] += 1

            if i + palindrome_length_at_index[i] > r:
                c, r = i, i + palindrome_length_at_index[i]

        maxLen, centerIndex = max((n, i) for i, n in enumerate(palindrome_length_at_index))
        palindrome_length_at_index.index(maxLen)
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


s = "cbbd"
s = "aacabdkacaa"
s = 'a'
test = Solution()
print(test.longest_palindrome(s))
