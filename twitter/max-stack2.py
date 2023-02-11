from collections import OrderedDict, Counter
from heapq import heappush, heappop


class MaxStack:
    def __init__(self):
        self.ordered = OrderedDict()
        self.max = []
        self.ref = Counter()

    def push(self, x):
        self.ref[x] += 1
        self.ordered[x] = x
        heappush(self.max, -x)

    def pop(self):
        try:
            k, v = self.ordered.popitem()
        except KeyError:
            return
        self.ref[v] -= 1
        if not self.ref[v]:
            del self.ref[v]
        return k

    def pop_max(self):
        while self.max and -self.max[0] not in self.ref:
            heappop(self.max)
        return -heappop(self.max) if self.max else -1

    def top(self):
        try:
            k, v = self.ordered.popitem()
        except KeyError:
            return
        while v not in self.ref:
            k, v = self.ordered.popitem()
        self.ordered[k] = v
        return v

    def peak_max(self):
        while self.max and -self.max[0] not in self.ref:
            heappop(self.max)
        if self.max:
            v = -self.max[0]
            self.ordered.move_to_end(self.ref[v])
            return v
        return -1


test = MaxStack()
test.pop()
test.pop_max()

test.push(1)
test.push(3)
test.push(2)
print(test.pop_max())
print(test.top())
test.pop()
print(test.peak_max())

