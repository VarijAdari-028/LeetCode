class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if s == "".join(sorted(s)):
            return 0
        if n == 2:                      # only allowed substrings have length 1
            return -1

        mn, mx = min(s), max(s)

        # 1 operation: sort everything except the first or last char
        if s[0] == mn or s[-1] == mx:
            return 1

        # 2 operations: need min somewhere in s[:-1], or max somewhere in s[1:]
        if mn in s[:-1] or mx in s[1:]:
            return 2

        # min only at the last position AND max only at the first position
        return 3