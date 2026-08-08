class Solution:
    def validSequence(self, word1: str, word2: str):
        ans = []

        # last[j] = the last index in word1 where
        # word2[j] can be matched while matching
        # word2[j:] as a subsequence.
        last = [-1] * len(word2)

        i = len(word1) - 1
        j = len(word2) - 1

        # Build last[] from right to left
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1

            i -= 1

        # We can use at most one mismatch
        canSkip = True
        j = 0

        # Greedily choose the smallest possible index
        for i, c in enumerate(word1):

            if j == len(word2):
                break

            # Normal exact match
            if c == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif canSkip and (
                j == len(word2) - 1 or i < last[j + 1]
            ):
                ans.append(i)
                j += 1
                canSkip = False

        return ans if j == len(word2) else []