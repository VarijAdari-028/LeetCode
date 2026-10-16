class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B1 = [0] * (n + 2)
        B2 = [0] * (n + 2)

        def add(b, i, v):
            while i <= n + 1:
                b[i] = (b[i] + v) % MOD
                i += i & -i

        def query(b, i):
            s = 0
            while i > 0:
                s += b[i]
                i -= i & -i
            return s % MOD

        def range_add(l, r, v):        # 1-indexed, inclusive
            add(B1, l, v)
            add(B1, r + 1, -v)
            add(B2, l, v * (l - 1))
            add(B2, r + 1, -v * r)

        def prefix(i):
            return (query(B1, i) * i - query(B2, i)) % MOD

        def range_sum(l, r):
            return (prefix(r) - prefix(l - 1)) % MOD

        last = {}
        S2 = 0
        ans = 0
        for j, x in enumerate(nums):
            p = last.get(x, -1)
            l, r = p + 2, j + 1        # indices (p, j] in 1-indexed form
            k = j - p
            S2 = (S2 + 2 * range_sum(l, r) + k) % MOD
            range_add(l, r, 1)
            ans = (ans + S2) % MOD
            last[x] = j
        return ans