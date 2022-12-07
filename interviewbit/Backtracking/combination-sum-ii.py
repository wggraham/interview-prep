import time

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        #each number only once
        A.sort()
        allCombos = []
        def getCombos(a, target, combo):
            if target < 0: return
            if target == 0 and combo not in allCombos:
                allCombos.append(combo)

            for i, v in enumerate(a):
                getCombos(a[i+1:], target - v, combo + [v])
        getCombos(A, B, [])
        return allCombos

    def combinationSum2(self, A, B):
        A.sort()
        allCombos = []
        root = Node(B)

        def getCombos(a, node, combo):
            if node.val == 0:
                allCombos.append(combo)

            for i, v in enumerate(a):
                if node.val < v:
                    break
                if v in node.children:
                    continue
                node.children[v] = Node(node.val - v)
                getCombos(a[i + 1:], node.children[v], combo + [v])

        getCombos(A, root, [])
        return allCombos

    def combinationSum3(self, A, B):
        A.sort()
        allCombos = []

        def getCombos(a, seen, combo, target):
            if target == 0:
                allCombos.append(combo)

            for i, v in enumerate(a):
                if target < v:
                    break
                if v in seen:
                    continue
                seen.add(v)
                getCombos(a[i + 1:], set(), combo + [v], target - v)

        getCombos(A, set(), [], B)
        return allCombos

    def permutationSum3(self, A, B):
        A.sort()
        allPerms = []

        def getPerms(a, seen, perm, target):
            if target == 0:
                allPerms.append(perm)

            for i, v in enumerate(a):
                if target < v:
                    break
                if v in seen:
                    continue
                seen.add(v)
                getPerms(a[:i] + a[i + 1:], set(), perm + [v], target - v)

        getPerms(A, set(), [], B)
        return allPerms


A = [10,1,2,7,6,1,5 ]
B = 8
test = Solution()
print(test.combinationSum(A, B))
print(test.combinationSum2(A, B))
print(test.combinationSum3(A, B))
print(test.permutationSum3(A, B))

test = Solution()
t0 = time.time()
test.combinationSum(A, B)
t1 = time.time()
test.combinationSum2(A, B)
t2 = time.time()
test.combinationSum3(A, B)
t3 = time.time()

print(t1-t0)
print(t2-t1)
print(t3-t2)