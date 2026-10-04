class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0

        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:  # '*' can be '(', ')' or empty
                lo -= 1
                hi += 1

            if hi < 0:        # too many ')' even if every '*' was '('
                return False
            lo = max(lo, 0)   # open count can't go negative

        return lo == 0        # can we end with zero unmatched '('?