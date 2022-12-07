from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        spaces = 1
        while i < len(words):
            total = len(words[i])
            j = i + 1
            while j < len(words) and total + (1 + len(words[j])) <= maxWidth:
                total += 1 + len(words[j])
                j += 1

            charsOnly = total - (j - i) + 1
            spaces = maxWidth - charsOnly
            spaceWidth = spaces // max((j - i - 1), 1)

            line = [words[i]]
            if j - i > 1:
                for k in range(spaces % (j - i - 1)):
                    i += 1
                    line += [' ' for _ in range(spaceWidth + 1)]
                    line += words[i]

            while i < j - 1 <= len(words) + 1:
                i += 1
                line += [' ' for _ in range(spaceWidth)]
                line += words[i]
            i += 1
            res.append(''.join(line))

        l = res.pop()
        l = l.split()
        l = ' '.join(l) + ''.join([' ' for _ in range(spaces - len(l) + 1)])
        return res + [l]


words = ["This", "is", "an", "example", "of", "text", "justification."]
#words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
test = Solution()
print(test.fullJustify(words, maxWidth))

# ["This   is   an", "example of text", "justification.  "]
# ['This    is    an','example of text', 'justification.  ']
# ['This    is    an','example  of text','justification.  ']
# ['This    is    an','example  of text','justification. ']
# ["This    is    an","example  of text","justification.  "]