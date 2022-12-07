import string


class Solution:
    def calculate(self, s: str) -> int:
        num, stack, prevOp, ops, digits = 0, [], '+', {'+', '-', '/', '*'}, set(string.digits)

        for c in s + '+':
            if c in digits:
                num = num * 10 + int(c)
                continue
            if c not in ops:
                continue

            match prevOp:
                case '+':
                    stack.append(num)
                case '-':
                    stack.append(-num)
                case '*':
                    stack.append(stack.pop() * num)
                case '/':
                    stack += [-(-stack.pop() // num)] if stack[-1] < 0 else [stack.pop() // num]
            prevOp, num = c, 0

        return sum(stack)


s = "3+2*2"
s = " 3+5 / 2 "
# s = " 3/2 "
test = Solution()
print(test.calculate(s))
