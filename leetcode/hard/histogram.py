def largestRectangleArea(height):
    height.append(0)
    s = []
    ans = 0
    for i, v in enumerate(height):
        while s and v < height[s[-1]]:
            h = height[s.pop()]
            w = i if not s else i - s[-1] - 1   # if stack empty everything left of current will be capped by this height
            ans = max(ans, w * h)
        s.append(i)
    return ans


a = [3, 2, 3, 7, 4, 1, 6, 5]
print(largestRectangleArea(a))
