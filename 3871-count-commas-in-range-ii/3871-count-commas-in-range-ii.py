class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        lo = 1000  # smallest 4-digit number, where commas start appearing
        d = 4
        while lo <= n:
            hi = min(n, lo * 10 - 1)
            commas_per_num = (d - 1) // 3
            count_in_range = hi - lo + 1
            total += commas_per_num * count_in_range
            lo *= 10
            d += 1
        return total