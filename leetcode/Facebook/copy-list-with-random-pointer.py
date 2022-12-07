from typing import Optional
from collections import defaultdict
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = defaultdict(Node)

        node = head
        while node:
            nodeMap[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            nodeMap[node].next = nodeMap[node.next] if node.next else None
            nodeMap[node].random = nodeMap[node.random] if node.random else None
            node = node.next

        return nodeMap[head]


root = Node(1)
root.next = Node(2)
root.random = root.next
root.next.random = root.next
test = Solution()
x = test.copyRandomList(root)
print(10)
