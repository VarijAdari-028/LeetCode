class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        # for each character's first occurrence, compute the minimal "closed" interval
        # (the smallest substring starting there that contains every occurrence of
        # every character it touches)
        intervals = []
        for i in range(n):
            c = s[i]
            if first[c] != i:
                continue  # only try starting an interval at a character's first occurrence

            end = last[c]
            j = i
            valid = True
            while j <= end:
                cj = s[j]
                if first[cj] < i:
                    valid = False  # this interval would need to reach before i — impossible
                    break
                end = max(end, last[cj])
                j += 1

            if valid:
                intervals.append((i, end))

        # greedy interval scheduling: pick smallest-end-first to maximize count;
        # since each candidate interval is already the minimal closed interval for
        # its start, this also yields minimum total length among max-count solutions
        intervals.sort(key=lambda x: x[1])

        result = []
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                result.append(s[start:end + 1])
                last_end = end

        return result