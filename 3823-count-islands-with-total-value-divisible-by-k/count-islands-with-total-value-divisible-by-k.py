class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        countRes = 0

        def dfs(r , c):

            #out of bounds 
            if r < 0 or r >= rows  or c < 0 or c >= cols or grid[r][c] == 0:
                return 0 
            
            if (r , c) in visit:
                return 0
            
            visit.add(( r, c))

            return ( grid[r][c] + dfs(r + 1 , c) + dfs(r - 1 , c) + dfs(r , c + 1) + dfs(r , c - 1))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r ,c) not in visit:
                    res = dfs(r , c)

                    if res % k == 0:
                        countRes += 1
        
        return countRes





        