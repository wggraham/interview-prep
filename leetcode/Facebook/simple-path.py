class Solution:
    # def simplifyPath(self, path: str) -> str:
    #     i = 0
    #     names = []
    #     n = len(path)
    #     while i < n:
    #         while i < n and path[i] == '/': i += 1
    #         j = i
    #         while i < n and path[i] == '.': i += 1
    #
    #         if i - j == 2:
    #             names.pop()
    #         elif i - j > 2:
    #             names.append(path[j:i])
    #         elif i - j == 1 and path[i] != '/':
    #             extension =

    def simplifyPath2(self, path: str) -> str:
        i = 0
        names = []
        n = len(path)
        while i < n:
            j = i
            while i < n and path[i] != '/' and path[i] != '.': i += 1

            names.append(path[j:i])
            while i < n and path[i] == '/': i += 1
            j = i
            while i < n and path[i] == '.': i += 1

            if i - j == 2:
                names.pop()
            elif i - j > 2:
                names.append(path[j:i])
            elif i - j == 1 and path[i] != '/':
                names[-2:] = names[-2] + names[-1]

        return '/'.join(names)

    def simplifyPath3(self, path: str) -> str:
        res = []
        for word in path.split('/'):
            if not word or word == '.':
                continue
            if word != '..':
                res.append(word)
            elif word == '..' and res:
                res.pop()

        return '/' + '/'.join(res)


path = "/home//foo/test.txt/"
test = Solution()
print(test.simplifyPath3(path))
