from math import gcd
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        for i in range(n):
            prod, g, l = 1, 0, 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if prod == g * l:
                    best = max(best, j - i + 1)

        return best