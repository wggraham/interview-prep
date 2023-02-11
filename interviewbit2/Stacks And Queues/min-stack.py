class MinStack:
    def __init__(self):
        self.stack = []
        self.min_vals = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        self.min_vals += [x] if not self.min_vals or x < self.min_vals[-1] else []

    # @return nothing
    def pop(self):
        if not self.stack: return
        if self.stack[-1] == self.min_vals[-1]:
            self.min_vals.pop()
        self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1] if self.stack else -1

    # @return an integer
    def getMin(self):
        return self.min_vals[-1] if self.min_vals else -1

