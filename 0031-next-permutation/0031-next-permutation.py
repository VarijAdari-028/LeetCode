class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # step 1: find the largest index i such that nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # step 2: find the largest index j > i such that nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # step 3: swap them
            nums[i], nums[j] = nums[j], nums[i]

        # step 4: reverse the suffix starting at i+1 (it's non-increasing, so this sorts it ascending)
        nums[i + 1:] = reversed(nums[i + 1:])