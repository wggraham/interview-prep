from typing import List


class Solution:
    def candy1(self, ratings: List[int]) -> int:
        up, down, total, peak = 1, 0, 1, 0

        for i in range(1, len(ratings)):
            if ratings[i - 1] >= ratings[i]:
                down += 1
                up = 1
                total += down + (peak <= down)
                continue

            up, down, peak, total = (1, 0, 0, total + up) if ratings[i - 1] == ratings[i] else (
            up + 1, 0, up + 1, total + up + 1)

        return total

    def candy2(self, ratings: List[int]) -> int:
        up, down, peak, total = 1, 0, 0, 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                up += 1
                down, peak = 0, up
                total += up
            elif ratings[i] == ratings[i - 1]:
                up, down, peak = 1, 0, 0
                total += 1
            else:
                down += 1
                up = 1
                total += down + (peak <= down)

        return total

    def candy3(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        if n > 1:
            if ratings[0] > ratings[1]:
                candies[0] = 2

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)
        # # def set_values(i):
        # #     if ratings[i - 1] > ratings[i] < ratings[i + 1]:
        # #         candies[i] = 1
        # #     elif ratings[i + 1] <= ratings[i]:
        # #         set_values(i + 1)
        # #
        # #
        # # ratings = [maxsize] + ratings + [maxsize]
        # # total = 0
        # # candies = [0] * len(ratings)


ratings = [1, 0, 2]
test = Solution()
print(test.candy2(ratings))
print(test.candy1(ratings))
