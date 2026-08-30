class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))

        if i > j:
            i, j = j, i

        # three strategies: both from front, both from back, or one from each side
        from_front = j + 1
        from_back = n - i
        front_and_back = (i + 1) + (n - j)

        return min(from_front, from_back, front_and_back)