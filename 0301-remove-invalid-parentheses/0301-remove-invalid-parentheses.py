class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Step 1: minimum removals
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        res = []
        n = len(s)

        def dfs(i, l_rem, r_rem, open_cnt, path):
            # Prune: more ')' than '(' kept so far
            if open_cnt < 0:
                return
            if i == n:
                if l_rem == 0 and r_rem == 0 and open_cnt == 0:
                    res.append("".join(path))
                return

            ch = s[i]

            if ch == '(' or ch == ')':
                # Group the run of identical parentheses starting at i
                j = i
                while j < n and s[j] == ch:
                    j += 1
                run = j - i

                # Choose how many from this run to remove (k), keep the rest
                rem = l_rem if ch == '(' else r_rem
                for k in range(0, min(run, rem) + 1):
                    kept = run - k
                    if ch == '(':
                        dfs(j, l_rem - k, r_rem, open_cnt + kept, path + ['('] * kept)
                    else:
                        dfs(j, l_rem, r_rem - k, open_cnt - kept, path + [')'] * kept)
            else:
                path.append(ch)
                dfs(i + 1, l_rem, r_rem, open_cnt, path)
                path.pop()

        dfs(0, left, right, 0, [])
        return res