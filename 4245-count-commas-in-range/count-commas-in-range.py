class Solution:
    def countCommas(self, n: int) -> int:
        # optimal sol

        res = 0
        power = 1000

        while power <= n:
            res += n - power + 1
            power *= 1000

        return res

        
        # optimal solution 

        if n < 1000:
            return 0 
        
        res = 0 
        start = 1000 
        comas = 1 

        while start <= n:
            end = min(n , start * 1000 - 1)

            res = (end - start + 1) * comas 

            start *= 1000 

            comas += 1
        return res

        








        # brute force 
        if n < 1000:
            return 0 

        res = 0
        
        for n in range(1000 , n + 1):
            length = len(str(n))

            res += (length - 1) // 3
        return res
        