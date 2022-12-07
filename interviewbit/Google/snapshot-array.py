from collections import defaultdict


class SnapshotArray:
    def __init__(self, length: int):
        self.snaps = [defaultdict(int)]

        for i in range(length):
            self.snaps[0][i] = 0

    def set(self, index: int, val: int) -> None:
        self.snaps[-1][index] = val

    def snap(self) -> int:
        self.snaps.append(defaultdict(int))
        return len(self.snaps) - 2

    def get(self, index: int, snap_id: int) -> int:
        for i in reversed(range(snap_id + 1)):
            if index in self.snaps[i]:
                return self.snaps[i][index]


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0,5)
print(obj.snap())
obj.set(0,6)
print(obj.get(0,0))
