class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # Pruning 1: board must contain enough of each letter
        from collections import Counter
        board_cnt = Counter(ch for row in board for ch in row)
        word_cnt = Counter(word)
        for ch, c in word_cnt.items():
            if board_cnt[ch] < c:
                return False

        # Pruning 2: start from the rarer end of the word
        if board_cnt[word[0]] > board_cnt[word[-1]]:
            word = word[::-1]

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False

            tmp = board[r][c]
            board[r][c] = '#'                      # mark visited in place

            found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or
                     dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))

            board[r][c] = tmp                      # restore (backtrack)
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False