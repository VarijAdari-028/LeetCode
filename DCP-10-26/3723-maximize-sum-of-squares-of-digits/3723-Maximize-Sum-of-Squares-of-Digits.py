class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        nines, rem = divmod(sum, 9)
        res = "9" * nines
        if rem:
            res += str(rem)
        res += "0" * (num - len(res))
        return res