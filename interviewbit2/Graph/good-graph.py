class Solution:
    def solve(self, a):
        def dfs(a):
            nonlocal ans
            flag, visited[a] = True, True
            for e in g[a]:
                if good[e]:
                    good[a] = True
                    return
                if visited[e]: continue

                flag = False
                dfs(e)

            good[a], ans = True, ans + int(flag)

        n, ans = len(a), 0
        g, visited, good = [[] for _ in range(n + 1)], [False] * (n + 1), [False] + [True] + [False] * (n - 1)
        for i, v in enumerate(a, 1):
            g[i].append(v)

        for i in range(1, n + 1):
            if visited[i] or good[i]: continue
            dfs(i)
        return ans

    def solve2(self, g):
        def get_sink(node):
            while g[node] != node:
                g[node] = g[g[node]]
                node = g[node]
            return node

        g, ans, visited, n = [0, 1] + g[1:], 0, set, len(g)
        for i in range(2, n):
            sink = get_sink(i)
            if sink != 1 and sink not in visited: ans += 1
            visited.add(sink)

        return ans

    def solve5(self, g):
        g, ans, visited, n = [0, 1] + g[1:], 0, set(), len(g)
        for i in range(2, n):
            sink = i
            while g[sink] != sink:
                sink = g[sink] = g[g[sink]]
            ans += int(sink != 1 and sink not in visited)
            visited.add(sink)

        return ans

    def _dfs(self, curr, graph, good_nodes, visited, moves):
        if curr in good_nodes:
            return

        visited[curr] = True
        next_node = graph[curr - 1]

        if next_node in good_nodes:
            good_nodes[curr] = 1
            return

        if not visited[next_node]:
            self._dfs(next_node, graph, good_nodes, visited, moves)
        else:
            good_nodes[next_node] = 1
            moves[0] += 1

        good_nodes[curr] = 1
        return

    def solve3(self, graph):
        good_nodes = {1: 1}
        num = len(graph)
        visited = [False] * (num + 1)
        moves = [0]

        for i in range(1, num + 1):
            self._dfs(i, graph, good_nodes, visited, moves)

        return moves[0]

    # def solve4(self, graph):
    def solve4(self, a):
        def dfs(a):
            nonlocal ans
            flag, visited[a] = False, True

            for e in g[a]:
                if good[e]:
                    good[a] = True
                    return
                if visited[e]: continue
                flag = True
                dfs(e)

            ans += not flag
            good[a] = True

        n = len(a)
        g = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        good = [False] * (n + 1)
        good[1] = True
        ans = 0
        for i in range(n):
            g[i + 1].append(a[i])
        for i in range(1, n + 1):
            if not visited[i] and not good[i]:
                dfs(i)
        return ans


A = [1, 2, 1, 2]
test = Solution()
print(test.solve(A))
# print(test.solve2(A))
print(test.solve3(A))
print(test.solve4(A))
print(test.solve5(A))
