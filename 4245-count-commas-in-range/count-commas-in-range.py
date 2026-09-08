class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0 
            
        res = 0
        
        for n in range(1000 , n + 1):
            length = len(str(n))

            res += (length - 1) // 3
        return res
        