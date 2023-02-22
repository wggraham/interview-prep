class Solution:
    def largestRectangleArea(self, nums):
        nums, s, area = [0] + nums + [0], [], 0
        for i, v in enumerate(nums):
            while s and nums[s[-1]] > v:
                j = s.pop()
                height, width = nums[j], i - s[-1] - 1
                area = max(area, height * width)

            s.append(i)

        return area
    #     def hist_area(nums):
    #         nums.append(0)
    #         s = []
    #         area = 0
    #         for i, v in enumerate(nums):
    #             s.append(i)
    #             while s and nums[s[-1]] >= v:
    #                 width, height = i - s[-1], nums[s.pop()]
    #                 area = max(area, height * width)
    #         return area
    #
    #     n, m = len(A), len(A[0])
    #     max_area = hist_area(A[0])
    #     for i in range(1, n):
    #         for j in range(m):
    #             A[i][j] = A[i][j] + A[i - 1][j] if A[i][j] else 0
    #         max_area = max(max_area, hist_area(A[i]))
    #
    #     return max_area


A = [2, 1, 5, 6, 2, 3]
A = [6, 2, 5, 4, 5, 1, 6]
test = Solution()
print(test.largestRectangleArea(A))
