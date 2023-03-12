class Solution:
    def strStr(self, A, B):
        match_val = 0
        for c in B:
            match_val *= 94
            match_val += ord(c) - ord(' ')
        hash_val = 0
        for c in A[:len(B)]:
            hash_val *= 94
            hash_val += ord(c) - ord(' ')
        if hash_val == match_val:
            return 0
        for i, c in enumerate(A[len(B):]):
            hash_val -= 94 ** (len(B) - 1) * (ord(A[i]) - ord(' '))
            hash_val *= 94
            hash_val += ord(c) - ord(' ')
            if hash_val == match_val:
                return i + 1

        return -1


A = "strstr"
B = "str"
A = "bigbit"
B = "bit"
A = "bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba"
B = "babaaa"
test = Solution()
print(test.strStr(A, B))
