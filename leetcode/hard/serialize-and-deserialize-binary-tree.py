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
        ser = []
        q = deque([root])

        while q:
            node = q.popleft()
            val = node.val if node else None
            ser.append(val)
            if node:
                q.extend([node.left, node.right])
        j = 0
        for i in range(len(ser)):
            if ser[-1 - i]:
                j = i
                break
        return ser[:-j] if not ser[-1] else ser

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root = TreeNode(data[0])
        q = deque([root])
        treeLst = deque(data[1:])
        while q and treeLst:
            node = q.popleft()
            val = treeLst.popleft()
            if val:
                node.left = TreeNode(val)
                q.append(node.left)
            if treeLst:
                val = treeLst.popleft()
                if val:
                    node.right = TreeNode(val)
                    q.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

a = [1,2,3,None,None,4,5]
test = Codec()
root = test.deserialize(a)
print(test.serialize(root))
