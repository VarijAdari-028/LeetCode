class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        n = len(sq)
        minus = n // 2                      # number of subtracted slots

        return sum(sq[minus:]) - sum(sq[:minus])