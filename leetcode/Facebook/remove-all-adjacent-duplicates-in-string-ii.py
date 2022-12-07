class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['', 0]]

        for c in s:
            if c != stack[-1][0]:
                stack += [[c, 0]]

            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()

        return ''.join([c * count for c, count in stack[1:]])


s = "abcd"
k = 2
s = "deeedbbcccbdaac"
k = 3
test = Solution()
print(test.removeDuplicates(s, k))
