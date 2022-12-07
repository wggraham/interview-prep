import heapq
import sys
import time
from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        s = deque([(0, 0, 1)])

        while s:
            ln, pos, speed = s.popleft()

            if pos == target:
                return ln

            # R case
            item = (ln + 1, pos, -1) if speed > 0 else (ln + 1, pos, 1)
            s.append(item)

            # A case
            s.append((ln + 1, pos + speed, speed * 2))

    def racecar_dp(self, target: int) -> int:
        s = deque([(0, 0, 1)])
        seen = set()

        while s:
            ln, pos, speed = s.popleft()

            if pos == target:
                return ln

            ln += 1
            # R case
            sp = -1 if speed > 0 else 1
            if (pos, sp) not in seen:
                seen.add((pos, sp))
                s.append((ln, pos, sp))

            # A case
            pos += speed
            speed *= 2
            if (pos, speed) not in seen:
                seen.add((pos, speed))
                s.append((ln, pos, speed))


    def racecar_bfs_optimized(self, target: int) -> int:
        queue = deque([(0, 0, 1)])

        while queue:
            moves, pos, speed = queue.popleft()

            if pos == target:
                return moves

            # A case
            queue.append((moves + 1, pos + speed, speed * 2))

            # R case
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                speed = -1 if speed > 0 else 1
                queue.append((moves + 1, pos, speed))
    dp = {0: 0}

    def racecar_dp_math(self, t):  # not mine
        if t in self.dp:
            return self.dp[t]

        n = t.bit_length()
        if 2 ** n - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar_dp_math(2 ** n - 1 - t) + n + 1   # get shortest path to 2^n - 1 - target
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar_dp_math(t - 2 ** (n - 1) + 2 ** m) + n + m + 1)
        return self.dp[t]

    def racecar_dp_math_iterative(self, target):
        dp = [0, 1, 4] + [sys.maxsize] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]

    def racecar_dijkstra(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [sys.maxsize] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps:
                continue

            for k in range(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ:
                    steps2 -= 1  # No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]

    def racecar_dijkstra2(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = {target: 0}

        while pq:
            steps, targ = heapq.heappop(pq)
            if targ in dist and dist[targ] > steps:
                continue

            for k in range(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ:
                    steps2 -= 1  # No "R" command if already exact

                if abs(targ2) <= barrier and (targ2 not in dist or dist[targ2] > steps2):
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]

test = Solution()
#print(test.racecar(330))
# t0 = time.time()
# print(test.racecar_dp(5478))
t1 = time.time()
print(test.racecar_bfs_optimized(54780))
t2 = time.time()
print(test.racecar_bfs_optimized(54780))
t3 = time.time()
# print(test.racecar_dp_math_iterative(54780))
# t4 = time.time()
# print(test.racecar_dijkstra(54780))
# t5 = time.time()
# print(test.racecar_dijkstra2(54780))
# t6 = time.time()
#print("racecar_dp: ", t1 - t0)
print("racecar_bfs_optimized: ", t2 - t1)
print("racecar_bfs_optimized: ", t3 - t2)
# print("racecar_dp_iterative: ", t4 - t3)
# print("racecar_dijkstra: ", t5 - t4)
# print("racecar_dijkstra2: ", t6 - t5)
