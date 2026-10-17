class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int) -> None:
            res.append(path[:])              # every path is a subset

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)             # only pick later elements
                path.pop()

        backtrack(0)
        return res