class Node:
    def __init__(self, k=0, v=0):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._move_to_head(self.cache[key])
            return

        if self.size == self.capacity:
            self.cache.pop(self.tail.prev.key)
            self._remove_node(self.tail.prev)
            self.size -= 1

        self.size += 1
        node = Node(key, value)
        self.cache[key] = node
        self._add_node(node)

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)


lRUCache = LRUCache(2)
print(lRUCache.put(2, 1))
print(lRUCache.put(2, 2))
print(lRUCache.get(2))
print(lRUCache.put(1, 1))
print(lRUCache.put(4, 1))
print(lRUCache.get(2))
