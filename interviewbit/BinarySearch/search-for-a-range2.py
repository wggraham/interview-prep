class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):

        def getLeft(a, b):
            start, end = 0, len(a) - 1
            while start <= end:
                mid = (start + end) >> 1
                if a[mid] == b:
                    if mid == 0 or a[mid-1] < b: return mid
                    else: end = mid - 1
                elif a[mid] < b:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        def getRight(a, b):
            start, end = 0, len(a) - 1
            while start <= end:
                mid = (start + end) >> 1
                if a[mid] == b:
                    if mid == len(a)-1 or a[mid+1] > b: return mid
                    else: start = mid + 1
                elif a[mid] > b:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        return [getLeft(A,B), getRight(A,B)]


A = [5, 7, 7, 8, 8, 10]
B = 8

A = [5, 17, 100, 111]
B = 3
test = Solution()
print(test.searchRange(A, B))
