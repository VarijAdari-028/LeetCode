class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i, n = 0, len(intervals)
        start, end = newInterval

        # 1. Intervals ending before newInterval starts
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals into newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        # 3. Remaining intervals start after newInterval ends
        while i < n:
            result.append(intervals[i])
            i += 1

        return result