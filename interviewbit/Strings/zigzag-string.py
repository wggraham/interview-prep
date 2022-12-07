class Solution:
    def convert(self, A, B):
        res = [[] for _ in range(B)]
        j, zig, k = -1, True, B - 1
        for i, c in enumerate(A):
            j += 1 if zig else -1
            if j == k and zig:
                zig = False
            if not j and not zig:
                zig = True
            res[j].append(c)

        return ''.join([y for x in res for y in x])


A = "PAYPALISHIRING"
B = 3
A = "kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS"
B = 1
test = Solution()
print(test.convert(A, B))
