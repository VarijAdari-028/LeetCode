class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                # Check if current sum is closer
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Move pointers
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current

        return closest