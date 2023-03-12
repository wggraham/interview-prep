class Solution:
    def atoi(self, A):
        word = A.strip().split()[0]
        j = i = 0 if word[0] != '+' and word[0] != '-' else 1
        sign = -1 if word[0] == '-' else 1
        while i < len(word) and word[i].isdigit(): i += 1
        res = int(word[j:i]) * sign if j != len(word) and word[j].isdigit() else 0
        return res if abs(res) < 2**31-1 else (sign * 2)**31

    def atoi2(self, A):
        A = A.strip().split()
        if A:
            A = A[0]
        else:
            return 0
        neg = False
        curr = 0
        if A[0] == '-':
            neg = True
            curr += 1
        if A[0] == '+':
            curr += 1

        result = 0
        while curr < len(A) and A[curr].isdigit():
            result = result * 10 + int(A[curr])
            curr += 1
        if neg:
            return -result if -result > -2 ** 31 else -2 ** 31
        else:
            return result if result < 2 ** 31 - 1 else 2 ** 31 - 1

A = "9a2aabb 2704"
A = "- 5 88C340185Q 71 8079 834617385 2898422X5297Z6900"
A = "35L 23792 5 0E468529 566523U14 36RG39"
A = "-54332872018247709407 4 54"
# A = "+7"
# A = "+4136YF3913 2 1568 8520 76288761844685 6701829 789U7626785718K68177"
# A = "+ 3611156"
# A = "D1 47 Q5"

test = Solution()
print(test.atoi(A))
print(test.atoi2(A))
