class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set() 
        res = 0
        def dfs(r , c):
            # Base Case 
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0" or (r, c) in visit:
                return 
            
            visit.add((r,c))

            dfs(r + 1 , c)
            dfs(r - 1 , c)
            dfs(r , c + 1)
            dfs(r , c - 1)



            
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r ,c)
                    res += 1
        return res
        