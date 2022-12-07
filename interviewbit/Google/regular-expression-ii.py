def __remove_redundant_items__(pattern):
    temp, i = [], 0
    while i < len(pattern):
        temp.append(pattern[i])

        if pattern[i] == '*':
            while i < len(pattern) and pattern[i] == '*':
                i += 1
            i -= 1
        i += 1
    return temp


class Solution:
    def isMatch(self, txt, pattern):
        pattern = __remove_redundant_items__(pattern)

        s = [(len(txt) - 1, len(pattern) - 1)]

        while s:
            i, j = s.pop()
            if i < 0 and j < 0:
                return 1
            if j < 0:
                return 0
            for k, c in reversed(list(enumerate(txt[:i + 1], i-1))):
                if pattern[j] == '*':
                    if j == 0:
                        return 1
                    j -= 1
                    l = k
                    while l >= 0:
                        if txt[l] == pattern[j] or pattern[j] == '.':
                            s.append((l - 1, j - 1))
                        l -= 1
                    # get all preceding chars
                elif pattern[j] == c or pattern[j] == '.':
                    j -= 1
                else:
                    break

        return 0


test = Solution()
print(test.isMatch("aab", "c*a*b"))
