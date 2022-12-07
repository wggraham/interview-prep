class Solution:
    def __getValue__(self, s):

        return 0

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack, i = [], 0
        ans = 0
        res = []
        while i < len(s):
            if s[i] == '(':
                stack.append([])
            elif s[i] == ')':
                res.append(self.__getValue__(stack.pop()))
            else:
                stack[-1].append(s[i])

        while stack:
            ans += self.__getValue__(stack.pop())

    def calculate2(self, s):
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))

            num, stack, sign = 0, [], "+"

            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)

    def calculate3(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0  # For the ongoing result
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':
                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand
                # Save the recently encountered '+' sign
                sign = 1
                # Reset operand
                operand = 0

            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':
                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':
                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop()  # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop()  # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand

    def calculate4(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0  # For the ongoing result
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)  # Forming operand, since it could be more than one digit
                continue
            elif ch == '+' or ch == '-':
                res += sign * operand
                sign = 1 if ch != '-' else -1  # Save the recently encountered '+' sign

            elif ch == '(':
                stack.append((sign, res))
                sign = 1
                res = 0

            elif ch == ')':
                res += sign * operand
                res = res * stack[-1][0] + stack[-1][1]
                stack.pop()
            operand = 0  # Reset the operand

        return res + sign * operand

    def calculate5(self, s: str) -> int:
        def getDigits(i):
            j, num = i, 0
            while j < len(s) and s[j].isdigit():
                num = num * 10 + int(s[j])
                j += 1
            return j, num

        ans, i, sign, stack = 0, 0, 1, []
        while True:
            i, num = getDigits(i)
            ans += num * sign
            if i == len(s):
                break
            if s[i] == '+' or s[i] == '-':
                sign = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                stack.append((sign, ans))
                ans, sign = 0, 1
            elif s[i] == ')':
                ans = stack[-1][0] * ans + stack[-1][1]
                stack.pop()
            i += 1
        return ans









s = "(1+(4+5+2)-3)+(6+8)"
# s = " 2-1 + 2 "
s = "(1+(4+5+2)-3)"
# s = "1 + 1"
# s = "- (3 + (4 + 5))"
# s = "-(3+(4+5))"
test = Solution()
print(test.calculate3(s))
print(test.calculate5(s))
