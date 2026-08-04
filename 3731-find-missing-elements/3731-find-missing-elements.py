from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        smallest = min(nums)
        largest = max(nums)

        return [x for x in range(smallest, largest + 1) if x not in nums_set]