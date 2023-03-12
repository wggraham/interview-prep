from collections import defaultdict
from functools import lru_cache


class Solution:
    def restoreIpAddresses(self, A):
        @lru_cache(None)
        def gen_ips(i, j, ip):
            if j > 4: return {}
            if i == n and j == 4:
                return {ip[:-1]}
            res = set()
            for k in range(i, min(n, i + 3)):
                val = int(A[i:k+1])
                if val > 255: break
                res.update(gen_ips(k + 1, j + 1, ip + A[i:k + 1] + '.'))
                if val == 0: break
            return res

        n = len(A)
        return list(gen_ips(0, 0, "")) if gen_ips(0, 0, "") else []

    def restoreIpAddresses2(self, A):
        def gen_ips(i, ip):
            if len(ip) > 4: return []
            if i == n and len(ip) == 4:
                return ['.'.join(ip)]
            res = []
            for k in range(i, min(n, i + 3)):
                val = int(A[i:k + 1])
                if val > 255: break
                res += gen_ips(k + 1, ip + [A[i:k + 1]])
                if val == 0: break
            return res

        n = len(A)
        return gen_ips(0, [])

    def restoreIpAddresses4(self, A):
        def gen_ips(i, ip):
            if len(ip) > 4: return []
            if i == len(A) and len(ip) == 4:
                return ['.'.join(ip)]
            res = []
            for k in range(i, min(len(A), i + 3)):
                val = int(A[i:k + 1])
                if val > 255 or (k > i and A[i] == '0'): break
                res += gen_ips(k + 1, ip + [A[i:k + 1]])
            return res

        return gen_ips(0, [])

    def restoreIpAddresses3(self, A):
        def generateIPs(A, idx):
            if len(curr_ip) == 4:
                if idx == n:
                    ips.append('.'.join(curr_ip))
                else:
                    return

            for i in range(idx, min(n, idx + 3)):
                num = int(A[idx:i + 1])
                if num > 255: break
                curr_ip.append(A[idx:i + 1])
                generateIPs(A, i + 1)
                curr_ip.pop()

                if num == 0:
                    break

        n, ips, curr_ip = len(A), [], []
        generateIPs(A, 0)

        return ips

    def restoreIpAddresses5(self, A):
        def validSegment(seg):
            return (len(seg) == 1 or seg[0] != '0') and int(seg) < 256

        iplist, n = [], len(A)
        for i in range(1, 4):
            if i >= n or not validSegment(A[:i]): break
            for j in range(i + 1, i + 4):
                if j >= n or not validSegment(A[i:j]): break
                for k in range(j + 1, j + 4):
                    if k + 1 > n: break
                    if not validSegment(A[j:k]) or not validSegment(A[k:]): continue
                    # iplist.append(A[:i] + '.' + A[i:j] + '.' + A[j:k] + '.' + A[k:])
                    iplist += ['.'.join([A[:i], A[i:j], A[j:k], A[k:]])]
        return iplist



A = "25525511135"
A = "0100100"
# A = "00000"
test = Solution()
print(test.restoreIpAddresses(A))
print(test.restoreIpAddresses2(A))
print(test.restoreIpAddresses3(A))
print(test.restoreIpAddresses4(A))
print(test.restoreIpAddresses5(A))
