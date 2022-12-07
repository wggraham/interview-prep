class Solution:
    def exist(self, board, word):
        if not board or not word:
            return 0

        n, m = len(board), len(board[0])
        visited = set()

        def inBounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def explore(i, j, k):
            if (i, j, k) in visited:
                return 0
            if k == len(word):
                return 1

            found = 0
            visited.add((i, j, k))
            adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for ii, jj in adj:
                y, x = i + ii, j + jj

                if not inBounds(y, x):
                    continue

                if board[y][x] == word[k]:
                    found |= explore(y, x, k + 1)

            return found

        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]:
                    continue

                if explore(i, j, 1):
                    return 1
        return 0


board = ["FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF"]
word = "BCDCB"
board = ["CCBBACCAACAAB", "ACACBCCAAAACA", "BCBCCBACACCBB", "BCCACCACCBCBB", "BACBABCCBCBBB", "BCACCACCCABCB",
         "CACABBBCABBAC", "ABBCAABBCBCCA", "ABBABABAACAAA", "AACCBCAACBBCA", "BCABCBBACCBAC", "CCABCABBBCBCC",
         "BCCACCABBABBA", "BCCCCCACBBABC", "CBCBBCCBBABAC", "ACCBBBCABCACA", "BCBABACCCAAAA", "BABBCBACCBBCC",
         "CBBBBCCBCABCC", "CCBBCBAACBBAB", "BBACBACCCBABC", "BABACBACCBCBA", "ABABCBBCBAAAC", "AABCAABBACCCB",
         "ABBCABCBACCAC", "ABBCACCCAAAAA", "BCCACABAACCBB", "BAABCCABABCCA", "CCAAABBCCBACC", "ABBAAABAABBAB",
         "BABBCACABBCAA", "AAABCCBCABABC", "ABBBABCACBBBA", "ACBBCAACACCCB", "BACBACCABAACA", "ABAABBCCAABBC",
         "ACBCCABBABAAB", "BBBCACCBCCBAA", "ABBCCABCCACBC", "CCABCBAACACBC", "BBCAACCCBABAB", "AABBCCCACCCAA",
         "CBAAACBCAACBC", "BCBCBCBBCCCBC", "CCABBCCCBAAAB", "CAABABACABACB", "CCABABCAABBBB", "CBCABBBACACBB",
         "BBACAABAACBBA", "BCCCCACCCBBCC", "BABCBCAAACBAA", "ABCAACBCBBCBC", "BAAAABACAACBA", "CCBBAAABCBCCA",
         "BACACBBBBBAAA", "CABCCCBCACCCA", "CCBCBAACAACAA", "CBACBABBCCCAB", "CCBCBCCBBBCAB", "CABAAAAACCCAC",
         "BBCCBABBBCCAC", "ABCABBAAAABCB", "BACABCBACACAA", "AABBABAABBBBC", "ABCAAAACCBCCA", "ACABBAACBCCCA",
         "CABCBCACAABBB", "CABAABCCABACA", "BABAABBAABACB", "CCACABACACCAC", "AAACABCCABAAB", "BAACBBAACCBAC",
         "AABAAAACCCCAA", "BCBACBCCCABAA", "CACBACABAABBB", "ABACCCBCBBAAB", "AAAAACCBBCAAB", "CACCCAAACAABB",
         "CBABCBBABBBCC", "CAACBBAABAABB", "ABBCCBBCBCBAA", "CABAAABAAABAB", "AABCBCCBCACCB", "CBBCCCBCABBAC",
         "BCACACCCCCABA", "CACABCCCCCBCC", "CABAAAABBCBAA", "AABBCBCBBCCAA", "CCBCCAACBBCAC", "AACCBAABBAAAA",
         "BAABCCACBCBCB"]
word = "CABABCBACABBCBAABACBACBBACCACABCCAABCCCBBBBCBCABBACABBCACCABBBBBACABCBBBCBCACCCA"

test = Solution()
print(test.exist(board, word))
