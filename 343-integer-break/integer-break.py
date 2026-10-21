class Solution:
    def integerBreak(self, n: int) -> int:
        #dp sol 

        dp = [0] * (n + 1)
        dp[1] = 1

        for num in range(2 , n + 1):
            dp[num] = 0 if num == n else num

            for i in range(1 , num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num] , val)

        return dp[n]


        #backtracking + cacheing 
        memo = {}
    

        def dfs(num):
            if num == 1:
                return 1
            
            if num in memo:
                return memo[num]
            
            res = 0 if num == n else num

            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                res = max(res , val)
            
            memo[num] = res
            return res

        return dfs(n)



        #backtracking brute force 
        def dfs(num):
            if num == 1:
                return 1
            
            res = 0 if num == n else num 

            for i in range( 1 , num):
                val = dfs(i) * dfs(num - i)
                res = max(res , val)
            return res

        return dfs(n)