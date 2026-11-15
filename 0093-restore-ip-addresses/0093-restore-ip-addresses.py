class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        parts = []

        # An IP needs 4 to 12 digits
        if n < 4 or n > 12:
            return res

        def backtrack(start: int) -> None:
            left = 4 - len(parts)             # segments still to place
            remaining = n - start
            if remaining < left or remaining > 3 * left:
                return                        # prune: can't fit the rest

            if left == 0:
                res.append(".".join(parts))
                return

            for length in range(1, 4):
                if start + length > n:
                    break
                seg = s[start:start + length]
                if len(seg) > 1 and seg[0] == '0':
                    break                     # leading zero: longer segments are invalid too
                if int(seg) > 255:
                    break                     # longer segments only get bigger
                parts.append(seg)
                backtrack(start + length)
                parts.pop()

        backtrack(0)
        return res