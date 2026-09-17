class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        queens = [-1] * n  # queens[row] = col

        def backtrack(row):
            if row == n:
                board = []
                for c in queens:
                    board.append('.' * c + 'Q' + '.' * (n - c - 1))
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens[row] = col

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            queens[row] = -1

        backtrack(0)
        return result