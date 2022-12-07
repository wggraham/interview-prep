from collections import OrderedDict


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        res = []
        seen = set()
        s = OrderedDict()
        for x in A:
            if x in s:
                s.pop(x)
            elif x not in seen:
                s[x] = None
            c = '#'
            if len(s) > 0:
                c, _ = s.popitem(False)
                s[c] = None
                s.move_to_end(c, False)
            seen.add(x)

            res.append(c)
        return ''.join(res)


test = Solution()
print(test.solve("jpxvxivxkkthvpqhhhjuzhkegnzqriokhsgea"))
