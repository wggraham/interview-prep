from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        d = deque([root])
        res = [root.val]
        while d:
            node = d.popleft()
            val = node.left.val if node.left else None
            res.append(val)
            val = node.right.val if node.right else None
            res.append(val)
            if node.left: d.append(node.left)
            if node.right: d.append(node.right)
        # truncate trailing nulls
        while not res[-1]: res.pop()
        return ','.join([str(x) if x else 'null' for x in res])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        root = TreeNode(data[0])
        d = deque([root])

        for i in range(1, len(data), 2):
            node = d.popleft()
            if data[i] != 'null':
                node.left = TreeNode(data[i])
                d.append(node.left)
            if data[i+1] != 'null':
                node.right = TreeNode(data[i+1])
                d.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

a = [1,2,3,None,None,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
test = Codec()
root = test.deserialize(a)
print(test.serialize(root))
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(ans)