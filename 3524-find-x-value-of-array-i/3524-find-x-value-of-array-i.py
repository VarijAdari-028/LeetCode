class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        # dp[v] = number of subarrays ending at the previous element with product % k == v
        dp = [0] * k

        for num in nums:
            m = num % k
            new_dp = [0] * k

            # extend every subarray ending at the previous element to include this one
            for v in range(k):
                if dp[v]:
                    new_dp[(v * m) % k] += dp[v]

            # the subarray consisting of just this element, on its own
            new_dp[m] += 1

            dp = new_dp
            for v in range(k):
                result[v] += dp[v]

        return result