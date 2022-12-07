from collections import defaultdict, deque


class Solution:
    def solve(self, A):
        root, edge_map = 0, defaultdict(list)
        for i, v in enumerate(A):
            edge_map[i].append(v)
            edge_map[v].append(i)
            if v == -1:
                root = i

        # bucket by levels
        levels, s = [{root}, {x for x in edge_map[root]}], [edge_map[root], 1]
        seen = {root}.update({x for x in edge_map[root]})
        while s:
            adj, depth = s.pop()
            level = set()
            for i in adj:
                for e in edge_map[i]:
                    if e in seen: continue
                    level.add(e)
                    seen.add(e)
            levels.append(level)

        # now you have the full set of nodes bucketed by level
        # if there are multiple at lowest level
        # return that depth * 2,

        deepest = len(levels) - 1
        n = len(levels)
        maxDist = n
        for i, level in enumerate(reversed(levels)):
            if len(level) > 1:
                maxDist = max(maxDist, (n - 1 - i) * 2)

        return maxDist

    def solve2(self, A):
        root, edge_map = 0, defaultdict(set)
        for i, v in enumerate(A):
            edge_map[i].add(v)

            if v != -1:
                edge_map[v].add(i)
                continue
            root = i

        # bucket by levels
        levels = [{root}, {x for x in edge_map[root]}]
        seen = {root}
        seen.update({x for x in edge_map[root]})
        while True:
            level = set()
            for i in levels[-1]:
                if i not in edge_map: continue
                for e in edge_map[i]:
                    if e in seen: continue
                    level.add(e)
                    seen.add(e)
            if not level: break
            levels.append(level)

        q = deque([[k, 0, len(levels) - 1] for k, v in edge_map.items() if len(v) == 1])

        for i in range(len(q)):
            node = q[i][0]
            for j, level in enumerate(levels):
                if node in level:
                    q[i][2] = j
                    break

        depth_map = defaultdict(int)
        dist_map = defaultdict(int)
        while q:
            node, depth, j = q.popleft()

            dist_map[node] = max(dist_map[node], depth_map[node] + depth)
            depth_map[node] = max(depth_map[node], depth)
            if node == root: continue
            q.extend([(i, depth + 1, j - 1) for i in edge_map[node] if i in levels[j - 1]])
        return max(dist_map.values())


A = [-1, 0, 0, 0, 3]
A = [ -1, 0, 1, 1, 2, 0, 5, 0, 3, 0, 0, 2, 3, 1, 12, 14, 0, 5, 9, 6, 16, 0, 13, 4, 17, 2, 1, 22, 14, 20, 10, 17, 0, 32, 15, 34, 10, 19, 3, 22, 29, 2, 36, 16, 15, 37, 38, 27, 31, 12, 24, 29, 17, 29, 32, 45, 40, 15, 35, 13, 25, 57, 20, 4, 44, 41, 52, 9, 53, 57, 18, 5, 44, 29, 30, 9, 29, 30, 8, 57, 8, 59, 59, 64, 37, 6, 54, 32, 40, 26, 15, 87, 49, 90, 6, 81, 73, 10, 8, 16 ]

test = Solution()
print(test.solve2(A))
