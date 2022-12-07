from queue import PriorityQueue
import heapq
import itertools

class Solution:
    def solve(self, A, B):
        A.sort(reverse=True)
        B.sort(reverse=True)
        res, n = [A[0] + B[0]], len(A)
        A, B = (B, A) if B[0] > A[0] else (A, B)
        i, j, i_back, j_back = 0, 1, 1, 0
        while len(res) < n:
            while len(res) < n and A[i] + B[j] >= A[i_back] + B[j_back]:
                res.append(A[i] + B[j])
                j += 1
            i, j, i_back, j_back = j_back, i_back, j, i
            A, B = B, A
        return res

    def solve1(self, A, B):
        A.sort(reverse=True)
        B.sort(reverse=True)
        res, n = [A[0] + B[0]], len(A)
        A, B = (B, A) if B[0] > A[0] else (A, B)
        i, j, i_back, j_back = 0, 1, 1, 0

        while len(res) < n:
            while len(res) < n and A[i] + B[j] >= A[i_back] + B[j_back]:
                res.append(A[i] + B[j])
                j += 1
            i, j, i_back, j_back = i_back, j_back, i, j
            # while len(res) < n and A[i] + B[j] >= A[i_back] + B[j_back]:
            #     res.append(A[i] + B[j])
            #     i += 1
            # i, j, i_back, j_back = i_back, j_back, i, j
        return res

    def solve2(self, A, B):
        A, B = sorted(A, reverse=True), sorted(B, reverse=True)
        n, result, visited, heap = len(A), [], {(0, 0)}, [(-(A[0] + B[0]), (0, 0))]

        for _ in range(n):
            total, (i, j) = heapq.heappop(heap)
            result.append(-total)

            if i < n - 1 and (i + 1, j) not in visited:
                heapq.heappush(heap, (-(A[i + 1] + B[j]), (i + 1, j)))
                visited.add((i + 1, j))

            if j < n - 1 and (i, j + 1) not in visited:
                heapq.heappush(heap, (-(A[i] + B[j + 1]), (i, j + 1)))
                visited.add((i, j + 1))

        return result

    def solve3(self, A, B):
        A.sort()
        B.sort()

        pq = PriorityQueue()

        s = set()

        n = len(A)
        pq.put((-1 * (A[n - 1] + B[n - 1]), (n - 1, n - 1)))
        s.add((n - 1, n - 1))
        res = list()

        for k in range(n):
            value = pq.get()
            sum_, i, j = value[0], value[1][0], value[1][1]
            res.append(-1 * sum_)
            idx_pair1 = (i - 1, j)
            pair1 = (-1 * (A[i - 1] + B[j]), idx_pair1)
            if idx_pair1 not in s:
                s.add(idx_pair1)
                pq.put(pair1)

            idx_pair2 = (i, j - 1)
            pair2 = (-1 * (A[i] + B[j - 1]), idx_pair2)
            if idx_pair2 not in s:
                s.add(idx_pair2)
                pq.put(pair2)

        return res


A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
A = [2, 4, 1, 1]
B = [-2, -3, 2, 4]
A = [36, 27, -35, 43, -15, 36, 42, -1, -29, 12, -23, 40, 9, 13, -24, -10, -24, 22, -14, -39, 18, 17, -21, 32, -20, 12,
     -27, 17, -15, -21, -48, -28, 8, 19, 17, 43, 6, -39, -8, -21, 23, -29, -31, 34, -13, 48, -26, -35, 20, -37, -24, 41,
     30, 6, 23, 12, 20, 46, 31, -45, -25, 34, -23, -14, -45, -4, -21, -37, 7, -26, 45, 32, -5, -36, 17, -16, 14, -7, 0,
     37, -42, 26, 28]
B = [38, 34, -47, 1, 4, 49, -18, 10, 26, 18, -11, -38, -24, 36, 44, -11, 45, 20, -16, 28, 17, -49, 47, -48, -33, 42, 2,
     6, -49, 30, 36, -9, 15, 39, -6, -31, -10, -21, -19, -33, 47, 21, 31, 25, -41, -23, 17, 6, 47, 3, 36, 15, -44, 33,
     -31, -26, -22, 21, -18, -21, -47, -31, 20, 18, -42, -35, -10, -1, 46, -27, -32, -5, -4, 1, -29, 5, 29, 38, 14, -22,
     -9, 0, 43]
# A = [48, 46, 45, 43, 43, 42, 41, 40, 37, 36, 36, 34, 34]
# B = [49, 47, 47, 47, 46, 45, 44, 43, 42, 39, 38, 38, 36]
# A = [3, 3, 2, 0, 0, 0]
# B = [7, 6, 5, 0, 0, 0]
test = Solution()
print(test.solve1(A, B))
print(test.solve2(A, B))

print(heapq.nlargest(len(A), [x + y for x, y in itertools.product(A, B)]))