class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')
                product = d1 * d2

                # position in result: digit at (i,j) contributes to indices (i+j) and (i+j+1)
                pos_low = i + j + 1
                pos_high = i + j

                total = product + result[pos_low]
                result[pos_low] = total % 10
                result[pos_high] += total // 10

        # skip leading zeros
        idx = 0
        while idx < len(result) - 1 and result[idx] == 0:
            idx += 1

        return ''.join(map(str, result[idx:]))