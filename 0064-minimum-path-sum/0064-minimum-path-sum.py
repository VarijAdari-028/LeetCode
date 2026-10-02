class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[0][0]
                elif i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]          # first row: only from the left
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]              # first column: only from above
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]  # above (old dp[j]) or left

        return dp[-1]