class Solution:
    def order(self, A, B):
        q = []
        people = sorted(zip(A, B), reverse=True)
        for p in people:
            q.insert(p[1], p[0])
        return q

