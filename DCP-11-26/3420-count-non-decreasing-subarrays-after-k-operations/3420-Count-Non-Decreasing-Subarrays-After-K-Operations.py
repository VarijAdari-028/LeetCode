from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:  # match your starter method name
        n = len(nums)
        pre = [0] * (n + 1)
        for i, v in enumerate(nums):
            pre[i + 1] = pre[i] + v

        dq = deque()      # segments [value, count]; left end = nearest to l
        S = 0             # sum of prefix maxima over window [l..r]
        r = n - 1
        ans = 0

        for l in range(n - 1, -1, -1):
            v = nums[l]
            cnt = 1
            while dq and dq[0][0] <= v:
                val, c = dq.popleft()
                S -= val * c
                cnt += c
            dq.appendleft([v, cnt])
            S += v * cnt

            # shrink from the right until the cost fits in k
            while S - (pre[r + 1] - pre[l]) > k:
                dq[-1][1] -= 1
                S -= dq[-1][0]
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1

            ans += r - l + 1

        return ans