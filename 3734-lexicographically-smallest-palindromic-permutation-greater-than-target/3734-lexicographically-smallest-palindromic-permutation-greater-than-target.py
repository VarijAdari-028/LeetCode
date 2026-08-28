class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        c = [0] * 26
        for ch in s:
            c[ord(ch) - 97] += 1

        if sum(x % 2 for x in c) > 1:
            return ""

        mid = ""
        half_cnt = c[:]
        for i in range(26):
            if half_cnt[i] % 2:
                mid = chr(97 + i)
                half_cnt[i] -= 1
            half_cnt[i] //= 2

        h = n // 2

        def counts_copy():
            return half_cnt[:]

        def left_exact():
            cnts = counts_copy()
            left_t = target[:h]
            for ch in left_t:
                idx = ord(ch) - 97
                if cnts[idx] == 0:
                    return None
                cnts[idx] -= 1
            if any(cnts):
                return None
            return left_t

        le = left_exact()
        if le is not None:
            if n % 2 == 0:
                cand = le + le[::-1]
                if cand > target:
                    return cand
            else:
                if mid > target[h]:
                    return le + mid + le[::-1]
                elif mid == target[h]:
                    cand = le + mid + le[::-1]
                    if cand > target:
                        return cand
                # mid < target[h]: fall through, deviate earlier

        for i in range(h - 1, -1, -1):
            cnts = counts_copy()
            ok = True
            for k in range(i):
                idx = ord(target[k]) - 97
                if cnts[idx] == 0:
                    ok = False
                    break
                cnts[idx] -= 1
            if not ok:
                continue

            t_idx = ord(target[i]) - 97
            chosen = -1
            for x in range(t_idx + 1, 26):
                if cnts[x] > 0:
                    chosen = x
                    break
            if chosen == -1:
                continue
            cnts[chosen] -= 1

            remaining = []
            for x in range(26):
                remaining.extend([chr(97 + x)] * cnts[x])
            remaining.sort()

            left = list(target[:i]) + [chr(97 + chosen)] + remaining
            left_str = ''.join(left)
            cand = left_str + (mid if n % 2 == 1 else "") + left_str[::-1]
            if cand > target:
                return cand

        return ""