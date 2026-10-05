class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i, n = 0, len(words)

        while i < n:
            # Greedily pick words [i, j) for this line
            j = i
            letters = 0
            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            count = j - i
            gaps = count - 1
            line_words = words[i:j]

            if j == n or gaps == 0:
                # Last line or single word: left-justify
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - letters
                base, extra = divmod(spaces, gaps)
                parts = []
                for k in range(gaps):
                    parts.append(line_words[k])
                    parts.append(" " * (base + (1 if k < extra else 0)))
                parts.append(line_words[-1])
                line = "".join(parts)

            res.append(line)
            i = j

        return res