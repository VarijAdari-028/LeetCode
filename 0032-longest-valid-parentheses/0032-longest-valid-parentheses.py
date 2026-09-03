class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # stack holds indices; start with -1 as a base for length calculations
        stack = [-1]

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # no matching '(' for this ')', so it becomes the new base
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len