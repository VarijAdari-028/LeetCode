class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        
        # dp[i][j] = set of possible balances at cell (i,j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0] = {1}  # grid[0][0] must be '(' (checked above)
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                delta = 1 if grid[i][j] == '(' else -1
                prev_balances = set()
                
                if i > 0:
                    prev_balances |= dp[i-1][j]
                if j > 0:
                    prev_balances |= dp[i][j-1]
                
                for b in prev_balances:
                    new_b = b + delta
                    if new_b >= 0:
                        dp[i][j].add(new_b)
        
        return 0 in dp[m-1][n-1]