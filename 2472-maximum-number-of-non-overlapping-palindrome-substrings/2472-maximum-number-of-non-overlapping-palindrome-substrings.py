class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # is_pal[i][j] = whether s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    is_pal[i][j] = (s[i] == s[j])
                else:
                    is_pal[i][j] = (s[i] == s[j]) and is_pal[i + 1][j - 1]

        dp = [0] * (n + 1)  # dp[i] = max count of valid palindromes using s[0:i]

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  # option 1: don't end a palindrome exactly at i-1
            for length in range(k, i + 1):
                start = i - length
                if is_pal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)
                    break  # see explanation below — this is a valid greedy shortcut

        return dp[n]