class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        self.minStack += [x] if not self.minStack or x <= self.minStack[-1] else []

    # @return nothing
    def pop(self):
        if not self.stack: return
        self.minStack = self.minStack[:-1] if self.stack[-1] == self.minStack[-1] else self.minStack
        self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1] if self.stack else -1

    # @return an integer
    def getMin(self):
        return self.minStack[-1] if self.minStack else -1



test = MinStack()
test.push(10)
test.push(9)
test.getMin()
test.push(8)
test.getMin()
test.push(7)
test.getMin()
test.push(6)
test.getMin()
test.pop()
test.getMin()
test.pop()
test.getMin()
test.pop()
test.getMin()
test.pop()
test.getMin()
test.pop()
test.getMin()
test.pop()