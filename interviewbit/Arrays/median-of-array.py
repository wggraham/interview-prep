class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        A, B = (B, A) if len(A) < len(B) else (A, B)
        n, m = len(A), len(B)
        step = m // 2
        i, j = n // 2 - 1, m // 2 - 1

        while step:
            if A[i] < B[j]:
                i += step
                j -= step
            else:
                i -= step
                j += step
            step //= 2

        if i < 0:
            i += 1
            j -= 1
        if j < 0:
            j += 1
            i -= 1

        mArr = [] # A[max(0, i - 1), min(n, i + 2)] + B[max(0, j - 1), min(m, j + 2)]
        for k in range(-1, 2):
            if 0 <= i+k < n:
                mArr.append((A[i+k], i+k, j-k))
            if 0 <= j+k < m:
                mArr.append((B[j+k], i-k, j+k))
        mArr.sort()

        l = len(mArr)
        if l % 2:
            return mArr[l//2][0] * 1.0

        if (m + n) % 2:
            return (mArr[l // 2][0] + mArr[l // 2 + 1][0]) / 2
        else:
            if mArr[l//2][0] <= B[mArr[l//2][2]]:
                return mArr[l//2][0] * 1.0
            else:
                return mArr[l//2 - 1][0] * 1.0



A = [ -50, -41, -40, -19, 5, 21, 28 ]
B = [ -50, -21, -10 ]
test = Solution()
print(test.findMedianSortedArrays(A, B))
