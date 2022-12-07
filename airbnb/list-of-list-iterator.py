class ArrayIterator:
    def __init__(self, arrs=None):
        self.arrs = arrs
        self.i, self.j = 0, 0

    def __iterate__(self):
        if self.j >= len(self.arrs[self.i]) - 1:
            self.i += 1
            self.j = -1
        self.j += 1

    def __goback__(self):
        if self.j != 0:
            self.j -= 1
            return

        if self.i == 0:
            return "error"

        self.i -= 1
        self.j = len(self.arrs[self.i]) - 1

    def has_next(self):
        return self.i < len(self.arrs) and self.j < len(self.arrs[self.i])

    def next(self):
        if not self.has_next():
            return "error"

        v = self.arrs[self.i][self.j]
        self.__iterate__()
        return v

    def remove(self):
        self.__goback__()

        if self.j == len(self.arrs[self.i]) - 1:
            self.arrs[self.i] = self.arrs[self.i][:-1]
            self.__iterate__()
            return

        if self.j == 0:
            self.arrs[self.i] = self.arrs[self.i][1:]
            return

        self.arrs[self.i] = self.arrs[self.i][:self.j] + self.arrs[self.i][self.j + 1:]


arrs = [[1, 2], [3]]    # [4, 5, 6]]
test = ArrayIterator(arrs)
print(test.has_next())
print(test.next())
print(test.has_next())
print(test.next())
test.remove()
print(test.has_next())
print(test.next())
# while test.has_next():
#     print(test.next())

# this doesn't explicitly handle when an array shrinks to size 0
