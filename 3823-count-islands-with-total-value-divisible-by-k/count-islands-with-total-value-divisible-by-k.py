class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # bfs solution 
        rows = len(grid)
        cols = len(grid[0])
        directions =[[0 , 1] , [1 , 0] , [-1 , 0] , [0 , -1]]
        visit = set()
        countRes = 0

        def bfs(r , c):
            q = collections.deque()
            q.append([r, c])
            visit.add((r , c))
            total = 0

            while q:
                r , c = q.popleft()
                total += grid[r][c]

                for dr , dc in directions:
                    nr = dr + r
                    nc = dc + c

                    # out of bounds or invalid
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0 or (nr , nc) in visit:
                        continue
                    
                    q.append([nr , nc])
                    visit.add((nr , nc))

            return total

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r , c) not in visit:
                    res = bfs(r , c)

                    if res % k == 0:
                        countRes += 1
        return countRes 

        # dfs solution
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        countRes = 0

        def dfs(r , c):

            # out of bounds 
            if r < 0 or r >= rows  or c < 0 or c >= cols or grid[r][c] == 0:
                return 0 
            
            if (r , c) in visit:
                return 0
            
            visit.add(( r, c))

            return (grid[r][c] + dfs(r + 1 , c) + dfs(r - 1 , c) + dfs(r , c + 1) + dfs(r , c - 1))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r ,c) not in visit:
                    res = dfs(r , c)

                    if res % k == 0:
                        countRes += 1
        
        return countRes





        