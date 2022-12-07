from collections import deque


class Solution:
    # @param A : list of integers
    # @return an integer
    # def jump(self, A):
    #     if not A or len(A) < 2:
    #         return 0
    #     seen = [False] * len(A)
    #     q = deque([(0, 1)])
    #     while q:
    #         i, depth = q.popleft()
    #
    #         for j in reversed(range(i + 1, min(A[i] + i + 1, len(A)))):
    #             if not seen[j]:
    #                 seen[j] = True
    #                 q.append((j, depth + 1))
    #             if j == len(A) - 1:
    #                 return depth
    #
    #     return -1

    def jump(self, A):
        if not A or len(A) < 2:
            return 0
        reachFrom = [0] * len(A)
        reachFrom[0] = 0
        hops = 1
        prev = 0
        for i, val in enumerate(A):
            if i + val >= len(A) - 1:
                return hops
            if reachFrom[prev] <= i:
                prev = i
                hops += 1
            reachFrom[i] = max(reachFrom[i], i + val)
        return -1
        # def dfs(i):
        #     global minJumpsFrom
        #     for j in range(i + 1, min(i + A[i], len(A))):
        #         if minJumpsFrom[j] == maxsize:
        #             dfs(j)
        #         minJumpsFrom[i] = min(minJumpsFrom[i], minJumpsFrom[j]) if minJumpsFrom[j] != -1 else minJumpsFrom[i]
        #
        # dfs(0)



test = Solution()
A = [2, 3, 1, 1, 4]
print(test.jump(A))
