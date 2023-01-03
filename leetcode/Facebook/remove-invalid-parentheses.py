from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def gen_valid_sub(i, j):
            k, count, part = i, 0, []
            while i <= j:
                if count and s[i] == ')':
                    part.append(s[k:i] + s[i + 1:j + 1])
                count += s[i] == '('
                count -= s[i] == ')'
                i += 1
            return part

        def combine(res, part):
            return [r + p for p in part for r in res]

        count, i, res = 0, 0, [""]
        for j, c in enumerate(s):
            count += c == '('
            count -= c == ')'

            if count < 0:
                res = combine(res, gen_valid_sub(i, j))
                count, i = 0, j + 1

        k = len(s) - 1
        while k > i and s[k] == '(':
            count -= 1
            k -= 1
        return [r + s[i:k + 1] for r in res] if res and count == 0 else [""]

    # bfs approach
    def removeInvalidParentheses2(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                count += (c == '(') - (c == ')')
                if count < 0:
                    return False

            return count == 0

        level = [s]
        while level:
            valid = {p for p in level if isValid(p)}
            if valid:
                return list(valid)

            level = [p[:i] + p[i+1:] for p in level for i in range(len(p)) if p[i] == '(' or p[i] == ')']

    # bfs approach optimized
    def removeInvalidParentheses4(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                count += (c == '(') - (c == ')')
                if count < 0:
                    return False

            return count == 0

        level = [s]
        while level:
            valid = {p for p in level if isValid(p)}
            if valid:
                return list(valid)

            level = [p[:i] + p[i + 1:] for p in level for i in range(len(p)) if p[i] == '(' or p[i] == ')']

    # leetcode, doesn't work
    def removeInvalidParentheses3(self, s):
        def isvalid(s):
            s = filter('()'.count, s)
            while '()' in s:
                s = s.replace('()', '')
            return not s

        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return list(valid)
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}

    def removeInvalidParentheses5(self, s) -> List[str]:
        def explore(i, l_count, r_count, l_rem, r_rem, p):
            if i == len(s):
                if l_rem == 0 and r_rem == 0:
                    result.add(''.join(p))
                return

            if s[i] != '(' and s[i] != ')':
                explore(i + 1, l_count, r_count, l_rem, r_rem, p + [s[i]])
            elif (s[i] == '(' and l_rem > 0) or (s[i] == ')' and r_rem > 0):
                explore(i + 1, l_count, r_count, l_rem - (s[i] == '('), r_rem - (s[i] == ')'), p)

            if s[i] == '(':
                explore(i + 1, l_count + 1, r_count, l_rem, r_rem, p + [s[i]])
            elif s[i] == ')' and l_count > r_count:
                explore(i + 1, l_count, r_count + 1, l_rem, r_rem, p + [s[i]])

        left, right, result = 0, 0, set()
        for c in s:
            left += c == '('
            right += left == 0 and c == ')'
            left -= left > 0 and c == ')'

        explore(0, 0, 0, left, right, [])
        return list(result)

    def removeInvalidParentheses7(self, s: str) -> List[str]:
        def dfs(s: List[str], starti: int, startj: int, parleft, parright) -> None:
            l_count = r_count = 0
            for i in range(starti, len(s)):
                l_count += s[i] == parleft
                r_count += s[i] == parright

                if r_count > l_count:
                    for j in range(startj, i + 1):
                        if s[j] != parright: continue
                        if j == startj or s[j - 1] != parright:
                            dfs(s[:j] + s[j + 1:], i, j, parleft, parright)
                    return

            if parleft == '(':
                dfs(s[::-1], 0, 0, ')', '(')
            else:
                res.append(''.join(s[::-1]))

        res = []
        dfs([c for c in s], 0, 0, '(', ')')
        return res

    def dfs(self, res: List[str], s: str, starti: int, startj: int, parleft, parright) -> None:
        parleftCount = 0
        parrightCount = 0
        for i in range(starti, len(s)):
            if s[i] == parleft:
                parleftCount += 1
            if s[i] == parright:
                parrightCount += 1
            if parrightCount > parleftCount:
                j = startj
                while j <= i:
                    if s[j] == parright and (j == startj or s[j - 1] != parright):
                        self.dfs(res, s[:j] + s[j + 1:], i, j, parleft, parright)
                    j += 1
                return
        reverse = s[::-1]
        if parleft == '(':
            self.dfs(res, reverse, 0, 0, ')', '(')
        else:
            res.append(reverse)
        return

    # def removeInvalidParentheses6(self, s: str) -> List[str]:
    #     left_count, right_count = 0, 0
    #     for c in s:
    #         left_count += c == '('
    #         right_count += c == ')'
    #
    #     def gen_valid_sub(i, j):
    #         k, count, part = i, 0, []
    #         while i <= j:
    #             if count and s[i] == ')':
    #                 part.append(s[k:i] + s[i + 1:j + 1])
    #             count += s[i] == '('
    #             count -= s[i] == ')'
    #             i += 1
    #         return part
    #
    #     def combine(res, part):
    #         return [r + p for p in part for r in res]
    #
    #     count, i, res = 0, 0, [""]
    #
    #     # q = deque([s])
    #     # while q:
    #
    #     for j, c in enumerate(s):
    #         count += c == '('
    #         count -= c == ')'
    #
    #         if count < 0:
    #             res = combine(res, gen_valid_sub(i, j))
    #             count, i = 0, j + 1
    #         if count and c == ')':
    #
    #     k = len(s) - 1
    #     while k > i and s[k] == '(':
    #         count -= 1
    #         k -= 1
    #     return [r + s[i:k + 1] for r in res] if res and count == 0 else [""]


s = "()())()"
s = "(a)())()"
# s = ")("
# s = "("
# s = "x("
# s = "(()"
s = "((()((s((((()"

test = Solution()
print(test.removeInvalidParentheses(s))
print(test.removeInvalidParentheses5(s))
print(test.removeInvalidParentheses7(s))
