def solution(A):
    def count_periods(i):
        if i > n - 2:
            return 0
        prev = A[i + 1]
        a = prev - A[i]
        counts = count_periods(i + 1)
        i += 2
        while i < n and A[i] - prev == a:
            prev = A[i]
            i += 1
            counts += 1
        return counts

    n = len(A)
    return count_periods(0)


def solution2(A):
    counts = 0
    for i in range(1, len(A)):
        a = A[i] - A[i - 1]
        for j in range(i + 1, len(A)):
            if A[j] - A[j - 1] != a: break
            counts += 1

    return counts if counts < 100000000 else -1


A = [1, 1, 2, 5, 7]
# A = [1, 3, 5, 7, 9]
# A = [7, 7, 7, 7]
# A = [3, -1, -5, -9]
# A = [0, 1]
A = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0, 1]
print(solution(A))
print(solution2(A))
