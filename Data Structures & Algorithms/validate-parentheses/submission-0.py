class Solution:
    def isValid(self, s: str) -> bool:
        closers = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack =[]
        for c in s:
            if c in closers:
                if not stack or stack[-1]!=closers[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        if not stack:    
            return True
        else: 
            return False
                        
