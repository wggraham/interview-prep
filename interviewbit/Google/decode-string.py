class Solution:
    def decodeString(self, s: str) -> str:
        def getDigits(i):
            j = i
            while i < n and s[i].isdigit():
                i += 1
            return int(s[j:i]), i - 1

        i, n, stack = 0, len(s), [[0, []]]
        val = 0
        while i < n:
            c = s[i]
            if c.isdigit():
                val, i = getDigits(i)
            elif c == '[':
                stack.append([val, []])
                val = 0
            elif c == ']':
                val, t = stack.pop()
                stack[-1][1] = stack[-1][1] + t * val
            else:
                stack[-1][1].append(s[i])
            i += 1

        return ''.join(stack[-1][1])


s = "3[a]2[bc]"
s = "2[abc]3[cd]ef"
# s = "3a"
test = Solution()
print(test.decodeString(s))
