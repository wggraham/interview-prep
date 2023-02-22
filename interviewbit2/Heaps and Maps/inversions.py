from bisect import bisect_right


class Solution:
    def countInversions(self, A):
        seen, count = [], 0
        for val in A:
            i = bisect_right(seen, val)
            seen.insert(i, val)
            count += len(seen) - i - 1
        return count

    def countInversions2(self, A):
        def merge_sort(a):
            if len(a) < 3:
                return (sorted(a), 1) if len(a) > 1 and a[1] < a[0] else (a, 0)
            l, l_count = merge_sort(a[:len(a) // 2])
            r, r_count = merge_sort(a[len(a) // 2:])
            count = l_count + r_count
            b, i, j, n, m = [], 0, 0, len(l), len(r)
            while True:
                if i == n:
                    b += r[j:]
                    break
                if j == m:
                    b += l[i:]
                    break
                if l[i] <= r[j]:
                    b.append(l[i])
                    i += 1
                else:
                    b.append(r[j])
                    j += 1
                    count += n - i

            return b, count

        return merge_sort(A)[1]


A = [59, 29]
A = [84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84,
     93, 67, 85, 16, 22, 60]
test = Solution()
print(test.countInversions(A))
print(test.countInversions2(A))
