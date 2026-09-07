class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last = [0] * 26  # last[c] = 1-indexed position of last occurrence, 0 if none

        for i in range(1, n + 1):
            c = ord(s[i - 1]) - ord('a')
            dp[i] = (2 * dp[i - 1]) % MOD
            if last[c] != 0:
                dp[i] = (dp[i] - dp[last[c] - 1]) % MOD
            last[c] = i

        return (dp[n] - 1) % MOD