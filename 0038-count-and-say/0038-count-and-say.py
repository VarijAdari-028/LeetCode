class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            next_result = []
            i = 0
            while i < len(result):
                j = i
                while j < len(result) and result[j] == result[i]:
                    j += 1
                next_result.append(str(j - i))
                next_result.append(result[i])
                i = j
            result = "".join(next_result)
        return result