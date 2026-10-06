class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0   # unmatched '(' so far
        added = 0         # insertions needed for unmatched ')'
        for ch in s:
            if ch == '(':
                open_needed += 1
            elif open_needed > 0:
                open_needed -= 1
            else:
                added += 1
        return added + open_needed