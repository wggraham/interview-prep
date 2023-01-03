from collections import OrderedDict


class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.lookup_table = {}

    def __add__(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def __remove__(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def __update__(self, node):
        self.__remove__(node)
        self.__add__(node)

    def __pop__(self):
        del self.lookup_table[self.tail.prev.key]
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def get(self, key: int) -> int:
        if key not in self.lookup_table:
            return -1
        self.__update__(self.lookup_table[key])
        return self.lookup_table[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup_table:
            node = self.lookup_table[key]
            node.val = value
            self.__update__(node)
            return

        self.capacity -= 1
        if self.capacity < 0:
            self.__pop__()

        self.lookup_table[key] = ListNode(key, value)
        self.__add__(self.lookup_table[key])


class LRUCache2(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)

        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class DLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache3:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        del self.cache[self.tail.prev.key]
        self._remove_node(self.tail.prev)

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
            self._move_to_head(self.cache[key])
            return

        self.cache[key] = DLinkedNode(key, value)
        self._add_node(self.cache[key])
        self.capacity -= 1

        if self.capacity < 0:
            self._pop_tail()



lRUCache = LRUCache(2)
print(lRUCache.put(2, 1))
print(lRUCache.put(2, 2))
print(lRUCache.get(2))
print(lRUCache.put(1, 1))
print(lRUCache.put(4, 1))
print(lRUCache.get(2))