class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_dot = seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True

            elif ch in "+-":
                # sign only at the start, or right after e/E
                if i > 0 and s[i - 1] not in "eE":
                    return False

            elif ch == ".":
                # no dot after another dot or after the exponent
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch in "eE":
                # need a digit before it, and only one exponent
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # need fresh digits after the exponent

            else:
                return False

        return seen_digit