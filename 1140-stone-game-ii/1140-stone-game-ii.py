class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones the current player
        # can collect starting from index i with current M
        dp = {}

        def solve(i, M):
            # Take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                # Stones opponent can get after we take X
                opponent = solve(i + X, max(M, X))

                # Total remaining stones - opponent's best
                current = suffix[i] - opponent

                best = max(best, current)

            dp[(i, M)] = best
            return best

        return solve(0, 1)