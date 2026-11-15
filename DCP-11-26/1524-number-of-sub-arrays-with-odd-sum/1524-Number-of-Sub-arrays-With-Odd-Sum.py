class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0      # empty prefix has sum 0 (even)
        parity = 0
        ans = 0

        for x in arr:
            parity ^= x & 1
            if parity:                 # prefix is odd: pair with earlier even prefixes
                ans += even
                odd += 1
            else:                      # prefix is even: pair with earlier odd prefixes
                ans += odd
                even += 1

        return ans % MOD