from sys import maxsize


class MinStack:
    def __init__(self):
        self.min_vals = []
        self.stack = []

    # @param x, an integer
    def push(self, x):
        if not len(self.min_val) or x <= self.min_vals[-1]:
            self.min_vals.append(x)
        self.stack.append(x)

    # @return nothing
    def pop(self):
        if not len(self.stack): return
        x = self.stack.pop()
        if x == min_vals[-1]:
            self.min_vals.pop()

    # @return an integer
    def top(self):
        return self.stack[-1] if len(self.stack) else -1

    # @return an integer
    def getMin(self):
        return self.min_vals[-1] if len(self.min_vals) else -1


