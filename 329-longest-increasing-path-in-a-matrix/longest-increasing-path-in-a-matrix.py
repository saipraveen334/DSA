class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [[0 , 1] , [1 , 0] , [0 , -1] , [-1 , 0]]
        memo = {}

        def dfs(r , c , prev):
            # out of bounds 
            if r < 0 or c < 0 or r == rows or c == cols or matrix[r][c] <= prev:
                return 0 
            
            if (r , c) in memo:
                return memo[(r , c)]

            res = 1

            for dr , dc in directions:
                nr = dr + r
                nc = dc + c

                res = max(res , 1 + dfs(nr , nc , matrix[r][c]))
            
            memo[(r , c)] = res
            return res

        k = 1
        for r in range(rows):
            for c in range(cols):
                k = max(k , dfs(r , c , -1))
        
        return k

            
            
        