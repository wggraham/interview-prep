import string


class Solution:
    def solve(self, A):
        words = A.split()
        if words[-1][-1] in string.punctuation:
            p = words[-1][-1]
            words[-1] = words[-1][:-1]
            words[0] = words[0] + p
        return ' '.join(words[::-1])


a = "the sky is blue."
test = Solution()
print(test.solve(a))
