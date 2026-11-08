class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # row column count approach 
        rowCnt = [0] * len(grid)
        colCnt = [0] * len(grid[0])
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowCnt[r] += 1
                    colCnt[c] += 1
            
        ans = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if rowCnt[r] > 1 or colCnt[c] > 1:
                        ans += 1
        return ans

        # dfs solution 
        ans = 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c, res):
            if (r, c) in visit or grid[r][c] == 0:
                return

            visit.add((r, c))
            res.add((r, c))

            for nc in range(cols):
                if grid[r][nc] == 1 and (r, nc) not in visit:
                    dfs(r, nc, res)

            for nr in range(rows):
                if grid[nr][c] == 1 and (nr, c) not in visit:
                    dfs(nr, c, res)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    k = set()
                    dfs(r, c, k)

                    if len(k) > 1:
                        ans += len(k)

        return ans