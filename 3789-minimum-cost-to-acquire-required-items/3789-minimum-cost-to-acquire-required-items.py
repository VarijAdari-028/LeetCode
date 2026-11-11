class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:  # match your starter method name
        def total(b: int) -> int:
            return b * costBoth + max(0, need1 - b) * cost1 + max(0, need2 - b) * cost2

        lo, hi = min(need1, need2), max(need1, need2)
        return min(total(0), total(lo), total(hi))