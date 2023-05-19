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

    def calculate2(self, s: str) -> int:
        num, stack, prevOp, ops, digits = 0, [], '+', {'+', '-', '/', '*'}, set(string.digits)

        for c in s + '+':
            if c in digits:
                num = num * 10 + int(c)
                continue
            if c not in ops:
                continue

            match prevOp:
                case '+' | '-':
                    stack += [num] if '+' else [-num]
                case '*':
                    stack.append(stack.pop() * num)
                case '/':
                    stack += [-(-stack.pop() // num)] if stack[-1] < 0 else [stack.pop() // num]
            prevOp, num = c, 0

        return sum(stack)

    def calculate3(self, s: str) -> int:
        def compute(exp):
            i = 0
            while i < len(exp) and exp[i] not in ops: i += 1
            num, op = (int(exp[:i]), exp[i]) if i < len(exp) else (int(exp[:i]), '')

            match op:
                case '+':
                    num += compute(exp[i + 1:])
                case '-':
                    num -= compute(exp[i + 1:])
                case '*':
                    num *= compute(exp[i + 1:])
                case '/':
                    num //= compute(exp[i + 1:])
                case '^':
                    num **= compute(exp[i + 1:])
            return num

        ops = {'+', '-', '/', '*', '^'}
        return compute(s)

s = "3+2*2"
s = " 3+5 ^ 2 * 3 "
# s = " 3/2 "
test = Solution()
# print(test.calculate(s))
print(test.calculate3(s))
