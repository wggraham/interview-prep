
class Node:
    def __init__(self, val=None, prev=None, nxt=None):
        self.prev = prev
        self.nxt = nxt
        self.val = val
        self.ref = None


def __remove__(node):
    try:
        node.prev.nxt = node.nxt
    except AttributeError:
        print("cannot pop empty stack")
        raise


class MaxStack:
    def __init__(self):
        self.stack = Node()
        self.max_stack = Node()

    def push(self, x):
        self.stack.nxt = self.stack = Node(x, self.stack)
        if self.max_stack.val is None or self.max_stack.val <= x:
            self.max_stack.nxt = self.max_stack = Node(x, self.max_stack)
            self.max_stack.ref = self.stack

    def pop(self):
        x = self.stack.val
        try:
            __remove__(self.stack)
        except AttributeError:
            return

        self.stack = self.stack.prev
        if x == self.max_stack.val:
            __remove__(self.max_stack)
            self.max_stack = self.max_stack.prev
        return x

    def pop_max(self):
        x = self.max_stack.val
        try:
            __remove__(self.max_stack)
        except AttributeError:
            return

        __remove__(self.max_stack.ref)
        self.max_stack = self.max_stack.prev

        return x

    def top(self):
        return self.stack.val

    def peak_max(self):
        return self.max_stack.val


test = MaxStack()
test.pop()
test.pop_max()

test.push(1)
test.push(3)
test.push(2)
print(test.pop_max())
print(test.top())
print(test.peak_max())

