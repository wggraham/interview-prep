from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def left_justify(i, j):
            width = maxWidth
            s = []
            for word in words[i:j]:
                width -= len(word)
                s.append(word)
                if width:
                    s.append(" ")
                    width -= 1
            for _ in range(width):
                s.append(" ")
            return ''.join(s)

        def left_right_justify(ccount, i, j):
            spaceWidth = (maxWidth - ccount + j - i +1) // (j - i)
            extraSpacesNeeded = maxWidth - ccount
            s = []
            for i, word in enumerate(words[i:j-1]):
                s.append(word)
                width = spaceWidth + 1 if i < extraSpacesNeeded else spaceWidth
                s += [" " for _ in range(width)]

            s += [words[j - 1]]
            return ''.join(s)

        res = []
        i = 0
        while i < len(words):
            count = len(words[i])
            j = i + 1
            while j < len(words) and count + len(words[j]) + 1 <= maxWidth:
                count += len(words[j]) + 1
                j += 1
                if j == len(words):
                    return res + [left_justify(i, j)]
            if j - i == 1:
                res += [left_justify(i, j)]
            else:
                res += [left_right_justify(count, i, j)]
            i = j
        return res

words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
test = Solution()
print(test.fullJustify(words, maxWidth))
