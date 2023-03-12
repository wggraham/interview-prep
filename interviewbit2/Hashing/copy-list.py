class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head):
        node_map = {head: RandomListNode(head.label)}
        s = [head]
        while s:
            node = s.pop()

            if node.next:
                if node.next not in node_map:
                    node_map[node.next] = RandomListNode(node.next.label)
                    s.append(node.next)
                node_map[node].next = node_map[node.next]
            if node.random:
                if node.random not in node_map:
                    node_map[node.random] = RandomListNode(node.random.label)
                    s.append(node.random)
                node_map[node].random = node_map[node.random]

        return node_map[head]


root = RandomListNode(1)
root.next = RandomListNode(2)
root.random = RandomListNode(3)
root.next.next = root.random
root.next.next.random = root
root.next.random = root

test = Solution()
x = test.copyRandomList(root)
print(10)
