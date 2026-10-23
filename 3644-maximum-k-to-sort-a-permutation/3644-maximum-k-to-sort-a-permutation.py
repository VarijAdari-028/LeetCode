class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1  # all bits set
        for i, x in enumerate(nums):
            if x != i:
                ans &= x
        return 0 if ans == -1 else ans