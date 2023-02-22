from collections import Counter
from sys import maxsize


def _stack_exists(s):
    if not s or s[-1] == -maxsize:
        raise IndexError


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = [-maxsize]
        self.on_stack = Counter()

    def _remove_stale_items(self):
        while self.stack and self.stack[-1] in self.on_stack and self.on_stack[self.stack[-1]] == 0:
            del self.on_stack[self.stack.pop()]

    def push(self, x):
        self.stack.append(x)
        self.max_stack += [x] if x >= self.max_stack[-1] else []
        self.on_stack[x] += 1

    def pop(self):
        try:
            self._remove_stale_items()
            _stack_exists(self.stack)

            val = self.stack.pop()
            self.on_stack[val] -= 1
            if not self.on_stack[val]:
                del self.on_stack[val]
            if val == self.max_stack[-1]:
                self.max_stack.pop()

            return val

        except IndexError:
            print("Stack is empty")

    def pop_max(self):
        try:
            _stack_exists(self.max_stack)
            self.on_stack[self.max_stack[-1]] -= 1
            return self.max_stack.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            _stack_exists(self.stack)
            return self.stack[-1]
        except IndexError:
            print("Stack is empty")

    def peak_max(self):
        try:
            _stack_exists(self.max_stack)
            return self.max_stack[-1]
        except IndexError:
            print("Stack is empty")


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
print(test.pop())
test.top()
test.pop()
