class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mod = 10 ** 9 + 7

        # if prev direction = 1 -- > move down 
        # if prev direction = 0 -- > move right 
        @cache
        def dfs(r , c , prev):
            # base case 
            if r == rows - 1 and c == cols - 1:
                return 1 
            
            res = 0

            if grid[r][c] == 1:

                if prev:
                    if r + 1 < rows:
                        res+= dfs(r + 1 , c , 0)
                else:
                    if c + 1 < cols:
                        res += dfs(r , c + 1 , 1)
            else:
                if r + 1 < rows:
                    res += dfs(r + 1 , c , 0)

                if c + 1 < cols:
                    res += dfs(r , c + 1 , 1)

            return res % mod

        k  = dfs(0 , 0 , -1)
        return k % mod
    
    
