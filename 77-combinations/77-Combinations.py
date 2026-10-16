class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                res.append(path[:])
                return

            # prune: need (k - len(path)) more numbers, so start can't exceed this
            for x in range(start, n - (k - len(path)) + 2):
                path.append(x)
                backtrack(x + 1)
                path.pop()

        backtrack(1)
        return res
    