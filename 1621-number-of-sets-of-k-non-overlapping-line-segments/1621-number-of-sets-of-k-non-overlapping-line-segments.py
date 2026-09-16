class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp0[i][j]: ways to place j segments among points 0..i, where point i is NOT covered by any segment
        # dp1[i][j]: ways to place j segments among points 0..i, where point i IS covered (endpoint or interior)
        dp0 = [[0] * (k + 1) for _ in range(n)]
        dp1 = [[0] * (k + 1) for _ in range(n)]

        dp0[0][0] = 1  # point 0, 0 segments, uncovered: exactly one way (do nothing)

        for i in range(1, n):
            for j in range(k + 1):
                # point i uncovered: point i-1 was either covered or uncovered, doesn't matter
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD

                if j >= 1:
                    # point i covered by segment j: either extend a segment already covering i-1,
                    # or start a fresh segment ending at i (whether i-1 was covered or not)
                    dp1[i][j] = (dp1[i - 1][j] + dp0[i - 1][j - 1] + dp1[i - 1][j - 1]) % MOD

        return (dp0[n - 1][k] + dp1[n - 1][k]) % MOD