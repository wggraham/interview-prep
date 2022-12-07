from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache2:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hMap = {}
        self.capacity = capacity + 1

    def __add(self, key, value):
        self.capacity -= 1
        node = Node(key, value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        return node

    def __remove(self, node):
        self.capacity += 1
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def __update(self, node):
        k, v = node.key, node.val
        self.__remove(node)
        return self.__add(k, v)

    def get(self, key: int) -> int:
        if key not in self.hMap: return -1
        self.hMap[key] = self.__update(self.hMap[key])
        return self.hMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hMap:
            self.hMap[key].val = value
            self.hMap[key] = self.__update(self.hMap[key])
        if key not in self.hMap:
            self.hMap[key] = self.__add(key, value)
            if not self.capacity:
                del self.hMap[self.tail.prev.key]
                self.__remove(self.tail.prev)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
lRUCache = LRUCache2(2)
print(lRUCache.put(2, 1))
print(lRUCache.put(2, 2))
print(lRUCache.get(2))
print(lRUCache.put(1, 1))
print(lRUCache.put(4, 1))
print(lRUCache.get(2))