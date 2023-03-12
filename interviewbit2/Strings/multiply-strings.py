class Solution:
    def multiply(self, A, B):
        res = 0
        B = "0" + B
        for i, c in enumerate(A):
            v1 = int(c)
            carry = 0
            temp = 0
            for j, c2 in enumerate(B[::-1]):
                v2 = int(c2)
                temp += ((v1 * v2 + carry) % 10) * (10 ** j)
                carry = (v1 * v2 + carry) // 10
            res += temp * 10 ** i
        return str(res)

    def multiply2(self, num1, num2):
        n, m = len(num1), len(num2)
        num1, num2, result = list(map(int, reversed(num1))), list(map(int, reversed(num2))), [0] * (n + m)

        for i in range(n):
            for j in range(m):
                result[i + j + 1] += (result[i + j] + num1[i] * num2[j]) // 10
                result[i + j] = (result[i + j] + num1[i] * num2[j]) % 10

        return ''.join(map(str, reversed(result))).lstrip('0')


A = "99999"
B = "99999"
# A = "999"
# B = "999"
test = Solution()
print(test.multiply(A, B))
print(test.multiply2(A, B))
