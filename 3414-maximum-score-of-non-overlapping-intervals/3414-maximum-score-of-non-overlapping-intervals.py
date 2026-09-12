from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rs = [intervals[i][1] for i in order]

        K = 4
        # dp[i][k] = (score, sorted list of original indices) — best result
        # using at most k non-overlapping intervals chosen from the first i
        # intervals (processed in increasing order of right endpoint)
        dp = [[(0, []) for _ in range(K + 1)] for _ in range(n + 1)]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] < b[1] else b

        for i in range(1, n + 1):
            orig_idx = order[i - 1]
            l, r, w = intervals[orig_idx]
            # count of already-processed intervals whose right endpoint < l
            p = bisect_left(rs, l, 0, i - 1)

            for k in range(K + 1):
                best = dp[i - 1][k]  # skip this interval
                if k >= 1:
                    prev_score, prev_indices = dp[p][k - 1]
                    new_score = prev_score + w
                    new_indices = sorted(prev_indices + [orig_idx])
                    best = better(best, (new_score, new_indices))
                dp[i][k] = best

        return dp[n][K][1]