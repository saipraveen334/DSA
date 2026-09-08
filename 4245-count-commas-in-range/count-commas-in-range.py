class Solution:
    def countCommas(self, n: int) -> int:

        # 1 line code 

        return max(n - 999 , 0)
        
        # optimal sol

        res = 0
        power = 1000

        while power <= n:
            res += n - power + 1
            power *= 1000

        return res


        # brute force 
        if n < 1000:
            return 0 

        res = 0
        
        for n in range(1000 , n + 1):
            length = len(str(n))

            res += (length - 1) // 3
        return res
        