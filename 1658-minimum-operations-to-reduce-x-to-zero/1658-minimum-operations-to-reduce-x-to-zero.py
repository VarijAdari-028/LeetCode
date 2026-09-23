class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        best_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                best_len = max(best_len, right - left + 1)

        return len(nums) - best_len if best_len != -1 else -1