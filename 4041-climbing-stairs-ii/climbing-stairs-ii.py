class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # backtracking + memoization 
        dp = {}
        
        def dfs(i):
            if i == n:
                return 0
            
            if i in dp:
                return dp[i]

            res = float("inf")

            for j in range(i + 1 , min(n , i + 3) + 1):
                res = min(res , costs[j - 1] + (j - i) ** 2 + dfs(j))
            
            dp[i] = res
            return dp[i]

        return dfs(0)




        # brute force

        def dfs(i):
            if i == n:
                return 0
            
            ans = float("inf")

            for j in range(i + 1 , min(n , i + 3) + 1):
                ans = min(ans , costs[j - 1] + (j - i) ** 2 + dfs(j))
            
            return ans 

        return dfs(0)
