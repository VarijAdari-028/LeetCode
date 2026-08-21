class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since the array is sorted, no possible
            # triplet can have sum 0
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result