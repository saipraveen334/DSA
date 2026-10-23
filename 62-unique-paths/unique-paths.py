class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # backtracking + cacheing 
        memo = {}
        res = 0

        def dfs(r , c):
            nonlocal res 

            if r == m - 1 and c == n -1:
                return 1

            if r >= m or c >= n:
                return 0 

            if (r , c) in memo:
                return memo[(r ,c)]
            
            res = dfs(r + 1 , c) + dfs(r , c + 1)
            
            memo[( r, c)] = res 
            return res

        return dfs(0 , 0)
            



        # backtracking sol 
        def dfs(r , c):
            if r == m - 1  and c == n - 1:
                return 1

            if r >= m or c >= n:
                return 0 

            return dfs(r + 1 , c) + dfs(r , c + 1)

        return dfs(0 , 0)         