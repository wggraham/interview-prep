class Solution:
    def trap(self, A):
        def getVolume(heights):
            volume, j, subtotal = 0, 0, 0
            for i, h in enumerate(heights[1:], 1):
                if h >= heights[j]:
                    volume, subtotal, j = volume + subtotal, 0, i
                subtotal += heights[j] - h
            return volume, j

        total, i = getVolume(A)
        total += getVolume(A[i:][::-1])[0]
        return total


A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
test = Solution()
print(test.trap(A))
