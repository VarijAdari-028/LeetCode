class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0  # next write position

        for x in nums:
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1

        return k