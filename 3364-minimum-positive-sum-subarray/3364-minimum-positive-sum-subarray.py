class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, v in enumerate(nums):
            pre[i + 1] = pre[i] + v

        best = float('inf')
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                s = pre[i + length] - pre[i]
                if 0 < s < best:
                    best = s

        return -1 if best == float('inf') else best