class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}

        def dfs(r , c):
            if r == rows:
                return 0
            
            if c < 0 or c == cols:
                return float("inf")
            
            if (r , c) in memo:
                return memo[(r, c)]
            
            ans = matrix[r][c] + min(dfs(r + 1 , c) , dfs(r + 1 , c + 1) , dfs(r + 1 , c - 1))

            memo[( r , c)] = ans 
            return ans
        
        res = float("inf")

        for c in range(cols):
            k = dfs(0, c)
            res = min(res , k)

        return res

            

        