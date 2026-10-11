class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(go_left: bool) -> int:
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    ans = mid              # record the match
                    if go_left:
                        hi = mid - 1       # keep looking further left
                    else:
                        lo = mid + 1       # keep looking further right
            return ans

        return [find(True), find(False)]