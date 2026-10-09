class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))  # row 0: build word2[:j] from "" by j inserts

        for i in range(1, m + 1):
            curr = [i] + [0] * n   # column 0: delete all i chars
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]              # chars match, no cost
                else:
                    curr[j] = 1 + min(
                        prev[j - 1],  # replace
                        prev[j],      # delete from word1
                        curr[j - 1],  # insert into word1
                    )
            prev = curr

        return prev[n]