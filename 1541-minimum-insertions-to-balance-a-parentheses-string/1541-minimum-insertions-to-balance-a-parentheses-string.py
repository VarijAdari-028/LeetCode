class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0   # insertions made
        need = 0  # right parens still required for open '('

        for ch in s:
            if ch == '(':
                # need is odd => a lone ')' is pending, so it must be completed first
                if need % 2 == 1:
                    res += 1      # insert ')' to finish the previous '('
                    need -= 1
                need += 2         # this '(' needs two ')'
            else:  # ch == ')'
                need -= 1
                if need == -1:    # ')' with no open '(', insert a '('
                    res += 1
                    need = 1      # that new '(' still needs one more ')'

        return res + need         # remaining need must be inserted