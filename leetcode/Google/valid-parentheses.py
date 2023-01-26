class Solution:
    def isValid(self, s: str) -> bool:
        square = paren = curly = 0

        for c in s:
            match c:
                case '(':
                    stack.append(c)
                case ')':
                    paren -= 1
                case '[':
                    square += 1
                case ']':
                    square -= 1
                case '{':
                    curly += 1
                case '}':
                    curly -= 1
            if paren < 0 or square < 0 or curly < 0:
                return False

        return all(count == 0 for count in [square, paren, curly])
    
    def isValid(self, s: str) -> bool:
        stack = []
        close = {'(':')','[':']','{':'}'}
        for c in s:
            match c:
                case '(' | '[' | '{':
                    stack.append(close[c])
                case ')' | ']' | '}':
                    if not stack or c != stack[-1]:
                        return False
                    stack.pop()

        return len(stack) == 0


s = "()[]{"
# s = "([)]"
s  = "()"
test = Solution()
print(test.isValid(s))
