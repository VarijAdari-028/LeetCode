class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def parseFactor(i):
            if expression[i] == '{':
                i += 1
                words, i = parseUnion(i)
                i += 1  # skip closing '}'
                return words, i
            else:
                j = i
                while j < n and expression[j].isalpha():
                    j += 1
                return {expression[i:j]}, j

        def parseConcat(i):
            factors = []
            while i < n and expression[i] not in ',}':
                f, i = parseFactor(i)
                factors.append(f)
            result = {''}
            for f in factors:
                result = {a + b for a in result for b in f}
            return result, i

        def parseUnion(i):
            words, i = parseConcat(i)
            result = set(words)
            while i < n and expression[i] == ',':
                i += 1
                words, i = parseConcat(i)
                result |= words
            return result, i

        result, _ = parseUnion(0)
        return sorted(result)