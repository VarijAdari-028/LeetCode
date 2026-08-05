class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        result = 0

        while x != 0:
            digit = abs(x) % 10

            if x < 0:
                digit = -digit

            x = int(x / 10)

            # Check overflow BEFORE adding digit
            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > 7
            ):
                return 0

            if result < -214748364 or (
                result == -214748364 and digit < -8
            ):
                return 0

            result = result * 10 + digit

        return result