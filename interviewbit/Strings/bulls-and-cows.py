from collections import Counter


class Solution:
    def solve(self, secret, guess):
        bull, cow = 0, 0
        sc = Counter(secret)
        for s, g in zip(secret, guess):
            bull += 1 if s == g else 0
            if g in sc and sc[g]:
                cow += 1
                sc[g] -= 1

        return str(bull) + 'A' + str(cow - bull) + 'B'


secret = "1807"
guess = "7810"
secret = "1123"
guess = "0111"
A = "785877522099603265383715887724199113622533163124491825161289881960986191463729657098643284370697763266372114430110332013593"
B = "904885340424515033093709365336315369010158804531609854601924408136541396093277767462789278845550756079393133213063820989463"

test = Solution()
print(test.solve(A, B))
