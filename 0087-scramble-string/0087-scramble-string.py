from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def solve(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):      # prune: letters must match
                return False

            n = len(a)
            for i in range(1, n):
                # no swap
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    return True
                # swap
                if solve(a[:i], b[n - i:]) and solve(a[i:], b[:n - i]):
                    return True
            return False

        return solve(s1, s2)