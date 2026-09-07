class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_mask = [0] * 9
        col_mask = [0] * 9
        box_mask = [0] * 9

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    d = int(c) - 1
                    box_idx = (i // 3) * 3 + (j // 3)
                    row_mask[i] |= (1 << d)
                    col_mask[j] |= (1 << d)
                    box_mask[box_idx] |= (1 << d)

        def backtrack(i, j):
            if i == 9:
                return True
            ni, nj = (i + 1, 0) if j == 8 else (i, j + 1)

            if board[i][j] != '.':
                return backtrack(ni, nj)

            box_idx = (i // 3) * 3 + (j // 3)
            used = row_mask[i] | col_mask[j] | box_mask[box_idx]

            for d in range(9):
                bit = 1 << d
                if used & bit:
                    continue

                board[i][j] = str(d + 1)
                row_mask[i] |= bit
                col_mask[j] |= bit
                box_mask[box_idx] |= bit

                if backtrack(ni, nj):
                    return True

                board[i][j] = '.'
                row_mask[i] &= ~bit
                col_mask[j] &= ~bit
                box_mask[box_idx] &= ~bit

            return False

        backtrack(0, 0)