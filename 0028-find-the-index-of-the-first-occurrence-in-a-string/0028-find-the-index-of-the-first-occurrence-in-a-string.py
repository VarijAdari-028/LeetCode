class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        # build the KMP failure (longest proper prefix-suffix) table
        fail = [0] * m
        k = 0
        for i in range(1, m):
            while k > 0 and needle[i] != needle[k]:
                k = fail[k - 1]
            if needle[i] == needle[k]:
                k += 1
            fail[i] = k

        k = 0
        for i in range(n):
            while k > 0 and haystack[i] != needle[k]:
                k = fail[k - 1]
            if haystack[i] == needle[k]:
                k += 1
            if k == m:
                return i - m + 1

        return -1