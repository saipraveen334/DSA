class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        # edge case 
        if grid[0][0] == ")":
            return False 
        
        memo = {}
        directions = [[1, 0] , [0 , 1]]

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r , c , countP):

            # invalid case 
            if countP < 0:
                return 
            
            # base case 
            if r == rows - 1 and c == cols - 1:
                return countP == 0 
            
            # cacheing 
            if (r ,c , countP) in memo:
                return memo[(r , c , countP)]
            
            for dr , dc in directions:
                nr = dr + r
                nc = dc + c

                # out of bounds condition
                if nr >= rows  or nc >= cols:
                    continue 
                
                if grid[nr][nc] == "(":
                    if dfs(nr , nc , countP + 1):
                        memo[(r , c , countP)] = True
                        return True 
                else:
                    if dfs(nr , nc , countP - 1):
                        memo[( r, c , countP)] = True 
                        return True 

            memo[(r, c, countP)] = False
            return False

        return dfs(0 , 0 , 1)
                





















        


        if grid[0][0] == ")":
            return False

        rows = len(grid)
        cols = len(grid[0])

        directions = [[1, 0], [0, 1]]

        def dfs(r, c, countPara):

            if countPara < 0:
                return False

            if r == rows - 1 and c == cols - 1:
                return countPara == 0

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr >= rows or nc >= cols:
                    continue

                if grid[nr][nc] == "(":
                    if dfs(nr, nc, countPara + 1):
                        return True
                else:
                    if dfs(nr, nc, countPara - 1):
                        return True

            return False

        return dfs(0, 0, 1)