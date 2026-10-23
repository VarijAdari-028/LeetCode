class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        best = 0

        def largest_in_histogram(h: List[int]) -> int:
            stack = []
            res = 0
            for i, cur in enumerate(h + [0]):      # sentinel 0 flushes the stack
                while stack and h[stack[-1]] >= cur:
                    height = h[stack.pop()]
                    left = stack[-1] if stack else -1
                    res = max(res, height * (i - left - 1))
                stack.append(i)
            return res

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            best = max(best, largest_in_histogram(heights))

        return best