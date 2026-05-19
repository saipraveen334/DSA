class Solution:
    def isValid(self, s: str) -> bool:

        cto={ ")":"(" ,"}":"{" , "]":"[" }
        stack=[]

        for c in s:
            if c in cto:
                if stack and stack[-1]==cto[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return False if stack else True