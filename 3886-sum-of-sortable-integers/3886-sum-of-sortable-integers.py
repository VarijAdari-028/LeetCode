class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            ok = True
            prev_max = float('-inf')

            for s in range(0, n, k):
                block = nums[s:s + k]

                # count cyclic descents in this block
                desc = 0
                for j in range(k - 1):
                    if block[j] > block[j + 1]:
                        desc += 1
                if block[-1] > block[0]:
                    desc += 1
                if desc > 1:
                    ok = False
                    break

                # blocks must already be in order relative to each other
                if min(block) < prev_max:
                    ok = False
                    break
                prev_max = max(block)

            if ok:
                total += k

        return total