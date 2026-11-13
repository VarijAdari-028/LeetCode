class Solution:
    def numDecodings(self, s: str) -> int:
        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = 1, 1 if s[0] != '0' else 0

        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':                       # single digit 1-9
                cur += prev1
            if 10 <= int(s[i - 1:i + 1]) <= 26:   # two digits 10-26
                cur += prev2
            prev2, prev1 = prev1, cur

        return prev1