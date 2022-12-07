import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
class Node:
    def __init__(self, sNum, next=None):
        self.sNum = sNum
        self.bNum = sNum
        self.next = next

    def remove(self):
        self.next = self.next.next


def findSignatureCounts(arr):
    # Write your code here
    total = 0
    head = node = Node(arr[0])
    totals = [0] * len(arr)
    for _ in range(len(arr)):
        node.next = node = Node(arr[node.sNum - 1])
    node.next = head
    # if arr[arr[i] - 1] == arr[i]
    node = head
    while head:
        total += 1
        temp = head.bNum
        while True:
            node.next.bNum, temp = temp, node.next.bNum
            if node.next.sNum == node.next.bNum:
                totals[node.next.sNum - 1] = total
                node.remove()

            node = node.next

            if node == head:
                break
        if node.next == node:
            totals[node.sNum - 1] = total
            break
    return totals


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    # arr_1 = [2, 1]
    # expected_1 = [2, 2]
    # output_1 = findSignatureCounts(arr_1)
    # check(expected_1, output_1)

    arr_2 = [1, 2]
    expected_2 = [1, 1]
    output_2 = findSignatureCounts(arr_2)
    check(expected_2, output_2)
