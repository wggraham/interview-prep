from collections import Counter
from time import *


class Solution:
    def majorityElement(self, A):
        counts = Counter(A)
        return counts.most_common(1)[0][0]

    def majorityElement2(self, A):
        a = (len(A) // 2)
        for i in A:
            if A.count(i) > a:
                return i

    def majorityElement3(self, A):
        maj = A[0]
        count = 1

        for v in A:
            count += 1 if v == maj else -1
            if count:
                continue

            count = 1
            maj = v

        return maj

    def majorityElement4(self, A):
        maj_element = A[0]
        count = 1

        for i in A:
            if i == maj_element:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_element = i
                count += 1
        return maj_element


a = [3, 1, 3, 4, 7, 3, 2, 2, 1, 4, 2, 2, 2, 2, 2, 2, 2]
test = Solution()
# print(test.majorityElement(a))
# print(test.majorityElement2(a))
# print(test.majorityElement3(a))
avg1 = 0
for _ in range(10000):
    t0 = time()
    test.majorityElement4(a)
    t1 = time()
    avg1 += (t1 - t0)

avg2 = 0
for _ in range(10000):
    t0 = time()
    test.majorityElement3(a)
    t1 = time()
    avg2 += (t1 - t0)

# test.majorityElement4(a)
# t2 = time()
# test.majorityElement2(a)
# t3 = time()
print(avg1)
print(avg2)

print(((avg1-avg2)/avg1)*100)