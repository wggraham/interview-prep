class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lca(self, A, B, C):
        def find_lca(node):
            if not node:
                return False, False, None
            found1, found2, val1 = find_lca(node.left)
            found1 = True if node.val == B else found1
            found2 = True if node.val == C else found2
            found3, found4, val2 = find_lca(node.right)
            found1 = found1 or node.val == B or found3
            found2 = found2 or node.val == C or found4
            val = val1 if val1 else val2
            val = node.val if found1 and found2 and not val else val

            return found1, found2, val

        _, _, res = find_lca(A)
        return res if res else -1

    def lca2(self, A, B, C):
        def find_lca(node):
            if not node:
                return False, False, None
            b1, c1 = node.val == B, node.val == C
            b2, c2, v2 = find_lca(node.left)
            b3, c3, v3 = find_lca(node.right)
            found_b, found_c = b1 or b2 or b3, c1 or c2 or c3
            val = v2 if v2 else v3

            return found_b, found_c, node.val if not val and found_b and found_c else found_b, found_c, val

        _, _, res = find_lca(A)
        return res if res else -1
