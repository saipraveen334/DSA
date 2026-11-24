class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        mod = 10 ** 9 + 7
        memo = {}

        def dfs(i , curSum):

            # base case 
            if i == n:
                if curSum == target:
                    return 1 
                else:
                    return 0
            
            if (i , curSum) in memo:
                return memo[(i , curSum)]

            res = 0 

            for num in range(1 , k + 1):
                res += dfs(i + 1 , curSum + num) 
                memo[(i , curSum)] = res
            
            memo[(i , curSum)] = res
            return res % mod

        return dfs(0 , 0) % mod
            
            
        