class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = {k: v for k, v in knowledge}
        result = []
        i, n = 0, len(s)
        
        while i < n:
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i+1:j]
                result.append(lookup.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1
        
        return ''.join(result)