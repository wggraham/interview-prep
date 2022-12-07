from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        front = [arr[0]]
        f= arr[0]
        for i in range(1, len(arr)):
            f ^= arr[i]
            front.append(f)

        for s, e in queries:
            res.append(front[e])
            if s > 0:
                res[-1] ^= front[s-1]

        return res

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
test = Solution()
print(test.xorQueries(arr, queries))
