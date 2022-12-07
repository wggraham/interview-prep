import bisect


class RangeModule(object):

    def __init__(self):
        self.X = [0, 10**9]
        self.track = [False] * 2

    def addRange(self, left, right, track=True):
        def index(x):
            i = bisect.bisect_left(self.X, x)
            if self.X[i] != x:
                self.X.insert(i, x)
                self.track.insert(i, self.track[i-1])
            return i
        i = index(left)
        j = index(right)
        self.X[i:j] = [left]
        self.track[i:j] = [track]

    def queryRange(self, left, right):
        i = bisect.bisect(self.X, left) - 1
        j = bisect.bisect_left(self.X, right)
        return all(self.track[i:j])

    def removeRange(self, left, right):
        self.addRange(left, right, False)


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10,20)
param_2 = obj.queryRange(14,16)
obj.removeRange(10,14)
obj.addRange(13,30)