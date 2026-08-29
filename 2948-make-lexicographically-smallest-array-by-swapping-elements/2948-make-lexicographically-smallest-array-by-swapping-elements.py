class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # sort values along with their original indices
        indexed = sorted(range(n), key=lambda i: nums[i])

        result = [0] * n
        i = 0
        while i < n:
            j = i
            # extend the group while consecutive sorted values are within `limit`
            while j + 1 < n and nums[indexed[j + 1]] - nums[indexed[j]] <= limit:
                j += 1

            # within this group, indices can be freely permuted (chain of swaps),
            # so place the sorted values back into the sorted original indices
            group_indices = sorted(indexed[i:j + 1])
            group_values = [nums[k] for k in indexed[i:j + 1]]

            for idx, val in zip(group_indices, group_values):
                result[idx] = val

            i = j + 1

        return result