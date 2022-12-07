from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if not root:
            return ""
        res = [root.val]
        q = deque([root])
        while q:
            node = q.popleft()
            l, r = 'null', 'null'
            if node.left:
                q.append(node.left)
                l = node.left.val
            if node.right:
                q.append(node.right)
                r = node.right.val
            res.extend([l, r])

        while res and res[-1] == 'null':
            res.pop()
        return ','.join([str(word) for word in res])

    def deserialize(self, data):
        if not data:
            return
        data = [word.strip() for word in data.split(',')]
        root = TreeNode(data[0])
        q = deque([root])
        i = 1
        while i < len(data):
            node = q.popleft()
            if data[i] != 'null':
                node.left = TreeNode(data[i])
                q.append(node.left)
            i += 1
            if i < len(data) and data[i] != 'null':
                node.right = TreeNode(data[i])
                q.append(node.right)
            i += 1
        return root


root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)
test = Codec()
a = "4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2"
# a = "5,4,7,3,null,2,null,-1,null,9"
a = "-1,0,1"
x = test.deserialize(a)
print(test.serialize(x))

ser = Codec()
deser = Codec()
x = ser.serialize(root)
print(x)
ans = deser.deserialize(ser.serialize(root))
print(ans)
