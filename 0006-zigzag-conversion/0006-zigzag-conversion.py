class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr = 0
        down = True

        for ch in s:
            rows[curr] += ch

            if curr == 0:
                down = True
            elif curr == numRows - 1:
                down = False

            if down:
                curr += 1
            else:
                curr -= 1

        return "".join(rows)