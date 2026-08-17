from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]
            ans = 0

            for k in range(l, r):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:
                    # Maximum possible result from this split is 2 * left_sum
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(l, k)
                    )

                elif left_sum > right_sum:
                    # From here onward right_sum only gets smaller,
                    # so if this split cannot improve ans, later ones won't either.
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, r)
                    )

                else:
                    ans = max(
                        ans,
                        left_sum + dfs(l, k),
                        right_sum + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)