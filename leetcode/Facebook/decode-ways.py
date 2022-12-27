from functools import lru_cache


class Solution:
    def numDecodingsRecursive(self, s: str) -> int:
        def ways(i):
            if i > n:
                return 0
            if i == n:
                return 1
            count = 0
            if s[i] != '0':
                count += ways(i + 1)
                if int(s[i:i + 2]) < 27:
                    count += ways(i + 2)
            return count

        n = len(s)
        return ways(0)

    def numDecodingsTopDown(self, s: str) -> int:
        def ways(i):
            if count_from[i] != -1:
                return count_from[i]
            if s[i] == '0':
                return 0
            count_from[i] = ways(i + 1)
            count_from[i] += ways(i + 2) if int(s[i:i + 2]) < 27 else 0
            return count_from[i]

        n = len(s)
        count_from = [-1] * n + [1, 0]
        return ways(0)

    def numDecodingsTopDownLRUImplicit(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def ways(i):
            if i > n - 2:
                return 1 if i == n or s[i] != '0' else 0
            if s[i] == '0':
                return 0

            return ways(i + 1) + ways(i + 2) if int(s[i:i + 2]) < 27 else ways(i + 1)

        n = len(s)
        return ways(0)

    def numDecodingsBottomUp(self, s: str) -> int:
        s += "00"
        ways_to = [0] * len(s)
        for i in range(len(s) - 2):
            ways_to[i + 1] += ways_to[i] if s[i + 1] != '0' else 0
            ways_to[i + 2] += ways_to[i] if s[i + 2] != '0' and int(s[i:i + 2]) < 27 else 0
        return ways_to[-1]

    def numDecodingsIterative(self, s: str) -> int:
        if len(s) == 1:
            return int(s[0] != '0')
        back = 1 if s[0] != '0' else 0
        back2 = 1 if s[0] != '0' and 0 < int(s[:2]) < 27 else 0
        for i, c in enumerate(s[2:], 2):
            back2 = back + back2 if 0 < int(s[:2]) < 27 else back
            back = back if c != '0' else back2
        return back + back2 if 0 < int(s[:2]) < 27 else back

    def numDecodingsIterative2(self, s: str) -> int:
        if s[0] == '0':
            return 0
        back, back2 = 1, 1
        for i in range(1, len(s)):
            temp = back if s[i] != '0' else 0
            if 9 < int(s[i - 1:i + 1]) < 27:
                temp += back2
            back2 = back
            back = temp
        return back

    def numDecodingsIterative3(self, s: str) -> int:
        if s[0] == '0': return 0
        back, back2 = 1, 1
        for i in range(1, len(s)):
            temp = back if s[i] != '0' else 0
            temp += back2 if 9 < int(s[i - 1:i + 1]) < 27 else 0
            back2 = back
            back = temp

        return back


s = "226"
# s = "06"
# s = '10'
# s = '60'
test = Solution()
print(test.numDecodingsRecursive(s))
print(test.numDecodingsTopDown(s))
print(test.numDecodingsBottomUp(s))
print(test.numDecodingsIterative(s))
print(test.numDecodingsIterative2(s))
print(test.numDecodingsIterative3(s))
