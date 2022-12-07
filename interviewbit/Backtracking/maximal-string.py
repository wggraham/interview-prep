from locale import atoi

maxVal = 0


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        if not A or not B:
            return

        def swap(s, a, m):
            global maxVal
            if atoi(s) > maxVal:
                maxVal = atoi(s)

            if not a or (s, a) in m:
                return
            m.add((s, a))

            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    newS = list(s)
                    newS[i], newS[j] = newS[j], newS[i]
                    swap(''.join(newS), a - 1, m)

        swap(A, B, set())

        return str(maxVal)


test = Solution()
print(test.solve("7599", 2))
