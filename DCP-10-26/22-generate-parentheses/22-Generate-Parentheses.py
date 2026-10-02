class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if open_count < n:               # can still add an opener
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()

            if close_count < open_count:     # can close only if an opener is unmatched
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return res