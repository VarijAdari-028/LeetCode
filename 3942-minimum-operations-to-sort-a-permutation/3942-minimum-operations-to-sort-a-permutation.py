class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float('inf')
        best = INF

        # Case A: ascending rotation, nums[i] = (i + r) % n
        r = nums[0]
        if all(nums[i] == (i + r) % n for i in range(n)):
            if r == 0:
                best = 0
            else:
                # rotate left n-r times, or Reverse, rotate left r times, Reverse
                best = min(n - r, r + 2)

        # Case B: descending rotation, nums[i] = (r - i) % n
        r = nums[0]
        if all(nums[i] == (r - i) % n for i in range(n)):
            k = (r + 1) % n
            # rotate left k times then reverse, or reverse then rotate left (n-k)%n times
            best = min(best, k + 1, 1 + (n - k) % n)

        return -1 if best == INF else best