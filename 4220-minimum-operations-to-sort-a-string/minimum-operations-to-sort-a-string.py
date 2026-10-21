class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        #if all are sorted 
        if all(s[i + 1] >= s[i] for i in range(len(s) -1)):
            return 0 
        
        if n == 2:
            return -1 
        
        smx = max(s)
        smi = min(s)

        if smx == s[-1] or smi == s[0]:
            return 1 
        
        for i in range( 1, n - 1):
            if s[i] == smx or s[i] == smi:
                return 2
        
        return 3
            