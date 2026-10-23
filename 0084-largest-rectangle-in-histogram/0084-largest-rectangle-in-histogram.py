class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices, heights strictly increasing from bottom to top
        best = 0

        for i, h in enumerate(heights + [0]):   # sentinel 0 flushes the stack
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                best = max(best, height * width)
            stack.append(i)

        return best