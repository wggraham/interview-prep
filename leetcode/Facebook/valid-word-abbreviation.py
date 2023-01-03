class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j, n, m = 0, 0, len(word), len(abbr)

        while i < n and j < m:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    break
                k = j
                while j < m and abbr[j].isdigit(): j += 1
                i += int(abbr[k:j])
            else:
                break
        return i == n and j == m


word = "internationalization"
abbr = "i12iz4n"
word = "apple"
abbr = "a2e"
# word = "internationalization"
# abbr = "i5a11o1"
# word = "hi"
# abbr = "hi1"
# word = "hi"
# abbr = "2i"
test = Solution()
print(test.validWordAbbreviation(word, abbr))
