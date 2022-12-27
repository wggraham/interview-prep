class Solution:
    def books(self, A, B):
        sum_to = [0]
        for v in A:
            sum_to.append(sum_to[-1] + v)
        sum_to = sum_to[1:]

        k = B


    def numberOfStudents(self, A, pages):
        count = 0
        students = 1
        for i in range(len(A)):
            count += A[i]
            if count > pages:
                count = A[i]
                students += 1
        return students

    def books2(self, A, B):
        if B > len(A):
            return -1
        min_pages = max(A)
        max_pages = sum(A)
        while min_pages < max_pages:
            mid = int((min_pages + max_pages) / 2)
            if self.numberOfStudents(A, mid) > B:
                min_pages = mid + 1
            else:
                max_pages = mid
        return min_pages

    def books3(self, A, B):
        def get_alloc(pages):
            page_count, students = 0, 1
            for p in A:
                page_count += p
                if page_count > pages:
                    page_count = p
                    students += 1
            return students

        if B > len(A):
            return -1

        min_pages, max_pages = max(A), sum(A) - B + 1
        while min_pages < max_pages:
            m = (min_pages + max_pages) // 2
            if get_alloc(m) > B:
                min_pages = m + 1
            else:
                max_pages = m
        return min_pages

A = [12, 34, 67, 90]
B = 2
A = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
B = 5
test = Solution()
print(test.books3(A, B))
print(test.books2(A, B))
