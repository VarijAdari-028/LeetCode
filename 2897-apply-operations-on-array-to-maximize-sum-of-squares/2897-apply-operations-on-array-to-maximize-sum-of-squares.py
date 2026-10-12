class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        # cnt[b] = how many numbers have bit b set (preserved by the operation)
        cnt = [0] * 30
        for x in nums:
            for b in range(30):
                if (x >> b) & 1:
                    cnt[b] += 1

        res = 0
        for _ in range(k):
            cur = 0
            for b in range(30):
                if cnt[b] > 0:
                    cur |= 1 << b
                    cnt[b] -= 1
            res = (res + cur * cur) % MOD

        return res