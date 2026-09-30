class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        answer = []
        
        for ch in seq:
            if ch == '(':
                answer.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                answer.append(depth % 2)
        
        return answer