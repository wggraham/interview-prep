class Solution:
    def convert(self, A, B):
        if B == 1: return A
        rev, j, rows = True, 0, [[] for _ in range(B)]
        for i, v in enumerate(A):
            rev = not rev if j == 0 or j == B - 1 else rev
            rows[j].append(v)
            j += -1 if rev else 1

        return ''.join(c for row in rows for c in row)


A = "paypalishiring"
B = 3
A = "kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS"
B = 1
test = Solution()
print(test.convert(A, B))
