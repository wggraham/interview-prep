from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def genLine():
            line = []
            for j, w in enumerate(words[i - wordCount:i-1]):
                space = spaceSize + 1 if j < extraSpaces else spaceSize
                line += [w] + [' ' for _ in range(space)]
            line += [words[i-1]]
            return line

        wordCount, charCount, res = 0, 0, []
        for i, word in enumerate(words):
            if (charCount + wordCount + len(word)) <= maxWidth:
                wordCount += 1
                charCount += len(word)
                continue

            spaces = maxWidth - charCount
            divisor = wordCount - 1 if wordCount > 1 else 1
            # spaceSize = spaces // divisor
            # extraSpaces = spaces % divisor
            spaceSize, extraSpaces = divmod(spaces, divisor)
            line = genLine()
            line += [' ' for _ in range(maxWidth - charCount - spaceSize * (wordCount - 1) - extraSpaces)]

            res.append(''.join(line))

            wordCount = 1
            charCount = len(word)

        i = len(words)
        spaceSize = 1
        extraSpaces = 0
        spaces = maxWidth - charCount - wordCount + 1
        line = genLine() + [' ' for _ in range(spaces)]

        return res + [''.join(line)]

    def fullJustify2(self, words: List[str], maxWidth: int) -> List[str]:

        result, current_list, num_of_letters = [], [], 0
        # result -> stores final result output
        # current_list -> stores list of words which are traversed but not yet added to result
        # num_of_letters -> stores number of chars corresponding to words in current_list

        for word in words:

            # total no. of chars in current_list + total no. of chars in current word
            # + total no. of words ~= min. number of spaces between words
            if num_of_letters + len(word) + len(current_list) > maxWidth:
                # size will be used for module "magic" for round robin
                # we use max. 1 because atleast one word would be there and to avoid modulo by 0
                size = max(1, len(current_list) - 1)

                for i in range(maxWidth - num_of_letters):
                    # add space to each word in round robin fashion
                    index = i % size
                    current_list[index] += ' '

                    # add current line of words to the output
                result.append("".join(current_list))
                current_list, num_of_letters = [], 0

            # add current word to the list and add length to char count
            current_list.append(word)
            num_of_letters += len(word)

        # form last line by join with space and left justify to maxWidth using ljust (python method)
        # that means pad additional spaces to the right to make string length equal to maxWidth
        result.append(" ".join(current_list).ljust(maxWidth))

        return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
#words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20

test = Solution()
print(test.fullJustify(words, maxWidth))
# ["What   must   be", "acknowledgment  ", "shall be        "]
# ['What   must   be', 'acknowledgment  ', 'shall be        ']
# ["This    is    an","example  of text","justification.  "]
# ["This    is    an","example  of text","justification.  "]
# ['This    is    an','example  of text','justification.  ']