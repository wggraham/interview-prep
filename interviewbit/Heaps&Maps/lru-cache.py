from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=True)

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
        elif not self.cap:
            self.cache.popitem()
        else:
            self.cap -= 1

        self.cache[key] = value


