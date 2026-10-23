class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        #backtracking + cacheing 
        rows = len(grid)
        cols = len(grid[0])
        memo = [[-1] * cols for _ in range(rows)]

        def dfs(r , c):
            if r == rows -1 and c == cols - 1:
                return grid[r][c]
            
            if r >= rows or c >= cols:
                return float("inf")
            
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = grid[r][c] + min( dfs(r + 1 , c) , dfs(r , c + 1))

            return memo[r][c]
            
        return dfs(0 , 0)
            


        rows = len(grid)
        cols = len(grid[0])

        def dfs(i , j):

            if i == rows - 1 and j == cols - 1:
                return grid[rows - 1][cols -1]

            if i >= rows or j >= cols:
                return float("inf")

            return grid[i][j] + min(dfs(i + 1 , j) , dfs(i , j + 1))
        return dfs(0 , 0) 
        