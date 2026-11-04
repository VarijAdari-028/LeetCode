from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:  # match your starter method name
        n = len(nums)
        vals = sorted(set(nums))
        rk = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)
        top = 1 << (m.bit_length() - 1)

        def upd(i, c, s):
            while i <= m:
                cnt[i] += c
                sm[i] += s
                i += i & -i

        def query(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        def kth(r):  # rank of the r-th smallest element
            pos, pw = 0, top
            while pw:
                if pos + pw <= m and cnt[pos + pw] < r:
                    pos += pw
                    r -= cnt[pos]
                pw >>= 1
            return pos + 1

        costs = []
        total = 0
        for i in range(n):
            upd(rk[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                upd(rk[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                r = kth((x + 1) // 2)
                med = vals[r - 1]
                c, s = query(r)
                costs.append(med * c - s + (total - s) - med * (x - c))

        INF = float('inf')
        prev = [0] * (n + 1)              # j = 0: zero cost
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + costs[i - x])
            prev = cur

        return prev[n]