class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
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