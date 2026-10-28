class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        V = 1024

        # dp[j] = set of XOR values reachable at the current row, column j (as a Python int bitmask)
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    src = 1                      # XOR value 0 before including start
                else:
                    src = 0
                    if i > 0:
                        src |= dp[j]             # from above
                    if j > 0:
                        src |= dp[j - 1]         # from left
                # new set = { x ^ v for x in src }
                cur = 0
                x = 0
                s = src
                while s:
                    low = s & -s
                    x = low.bit_length() - 1
                    cur |= 1 << (x ^ v)
                    s ^= low
                dp[j] = cur

        mask = dp[-1]
        return (mask & -mask).bit_length() - 1   # lowest set bit = minimum XOR