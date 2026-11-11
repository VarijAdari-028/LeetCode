class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def backtrack(start: int) -> None:
            res.append(path[:])                      # every path is a subset

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue                         # same value already tried at this level
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res