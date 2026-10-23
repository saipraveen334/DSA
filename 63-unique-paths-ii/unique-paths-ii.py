class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        #backtracking + cacheing 
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        memo = [[-1] * cols  for _ in range(rows)]

        def dfs(r , c):
            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0

            if r == rows - 1 and  c == cols -1:
                return 1
            
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = dfs(r + 1, c) + dfs(r , c + 1)
            return memo[r][c]

        return dfs(0 , 0)
            


        #backtracking 
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return 1

            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0 

            return dfs(r + 1 , c) + dfs(r , c + 1)
        return dfs(0 , 0)
        