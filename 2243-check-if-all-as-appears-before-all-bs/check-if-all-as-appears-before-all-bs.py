class Solution:
    def checkString(self, s: str) -> bool:
        flag = False 
        
        for c in s:
            if c == 'b':
                flag = True 
            
            if flag:
                if c == 'a':
                    return False 
        return True 

        