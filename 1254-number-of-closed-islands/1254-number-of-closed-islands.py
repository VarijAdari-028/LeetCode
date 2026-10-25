class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def sink(r: int, c: int) -> None:
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                i, j = stack.pop()
                for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                        grid[ni][nj] = 1
                        stack.append((ni, nj))

        # Step 1: remove every island that touches the border
        for i in range(m):
            for j in range(n):
                if (i in (0, m - 1) or j in (0, n - 1)) and grid[i][j] == 0:
                    sink(i, j)

        # Step 2: each remaining component of 0s is a closed island
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                    sink(i, j)

        return count