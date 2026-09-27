class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        
        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                top = stack.pop()
                top.reverse()
                stack[-1].extend(top)
            else:
                stack[-1].append(ch)
        
        return ''.join(stack[0])