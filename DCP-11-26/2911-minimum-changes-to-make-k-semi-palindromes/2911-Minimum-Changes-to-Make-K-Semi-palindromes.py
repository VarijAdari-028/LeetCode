class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # divisors[L] = proper divisors d of L (d < L)
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for L in range(2 * d, n + 1, d):
                divisors[L].append(d)

        # cost[i][j] for substring s[i..j]
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divisors[L]:
                    changes = 0
                    m = L // d                      # size of each group
                    for g in range(d):              # group g: i+g, i+g+d, ...
                        for t in range(m // 2):
                            if s[i + g + t * d] != s[i + g + (m - 1 - t) * d]:
                                changes += 1
                    if changes < best:
                        best = changes
                cost[i][j] = best

        # dp[p][j]: first j chars split into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] < INF and cost[i][j - 1] < INF:
                        v = dp[p - 1][i] + cost[i][j - 1]
                        if v < dp[p][j]:
                            dp[p][j] = v

        return dp[k][n]