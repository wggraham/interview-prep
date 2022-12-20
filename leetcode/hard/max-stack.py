from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=None, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class MaxStack:

    def __init__(self):
        self.stack = ListNode()
        self.heap = []
        self.on_stack = set()
        self.tick = 0

    def __remove_stale__(self):
        while self.heap and self.heap[0][2].val[1] not in self.on_stack:
            heappop(self.heap)

    def push(self, x: int) -> None:
        self.__remove_stale__()
        self.stack.prev = self.stack = ListNode((x, self.tick), self.stack)
        heappush(self.heap, (-x, -self.tick, self.stack))
        self.on_stack.add(self.tick)
        self.tick += 1

    def pop(self) -> int:
        while self.stack and self.stack.val[1] not in self.on_stack:
            self.stack = self.stack.nxt
        x, tick = self.stack.val
        self.on_stack.remove(tick)
        self.__remove_stale__()
        self.stack = self.stack.nxt
        return x

    def top(self) -> int:
        return self.stack.val[0]

    def peekMax(self) -> int:
        self.__remove_stale__()
        return -self.heap[0][0]

    def popMax(self) -> int:
        self.__remove_stale__()
        x, _, ref = heappop(self.heap)
        self.on_stack.remove(ref.val[1])
        if ref == self.stack:
            self.stack = ref.nxt
        else:
            ref.prev.nxt = ref.nxt

        return -x


# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(-100)
obj.push(-91)
obj.push(34)
obj.push(1)
print(obj.pop())
print(obj.popMax())
print(obj.peekMax())
print(obj.top())
