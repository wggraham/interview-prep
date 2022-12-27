from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vect = []
        for i, v in enumerate(nums):
            if v == 0: continue
            self.vect.append((i, v))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        j, ans = 0, 0
        for i, v in vec.vect:
            while j < len(self.vect) and self.vect[j][0] < i:
                j += 1
            if j == len(self.vect):
                break
            if self.vect[j][0] != i: continue
            ans += self.vect[j][1] * v
        return ans


nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
print(ans)