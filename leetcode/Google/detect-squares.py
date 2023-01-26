from collections import defaultdict, Counter
from typing import List


class DetectSquares:

    def __init__(self):
        self.x_coord = defaultdict(Counter)
        self.y_coord = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_coord[x][y] += 1
        self.y_coord[y][x] += 1

    def count(self, point: List[int]) -> int:
        total = 0
        x, y = point
        for x1, count in self.y_coord[y].items():
            if x == x1:
                continue

            dx = abs(x1 - x)
            m1 = self.x_coord[x1][y - dx] * self.x_coord[x][y - dx]
            m2 = self.x_coord[x1][y + dx] * self.x_coord[x][y + dx]
            total += count * (m1 + m2)

        return total


class DetectSquares2:
    def __init__(self):
        self.counts = Counter()

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        total = 0
        x1, y1 = point
        for (x2, y2), count in self.counts.items():
            if x1 == x2 or abs(x1 - x2) != abs(y1 - y2):
                continue  # Skip empty square or invalid square point!
            total += count * self.counts[(x1, y2)] * self.counts[(x2, y1)]
        return total


# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
print(obj.count([11, 10]))
print(obj.count([14, 8]))
obj.add([11, 2])
print(obj.count([11, 10]))
