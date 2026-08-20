class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # BFS APPROACH 
        directions = [[0 , -1 ] , [1 , 0] , [ -1 , 0] , [0 ,1]]
        area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r , c))
            res = 1

            while q:
                row, col = q.popleft()

                for dr , dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == 0:
                        continue 
                    q.append((nr , nc))
                    grid[nr][nc] = 0
                    res += 1
            return res
                

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = max(area , bfs(r , c))
        return area













        # DFS APPROACH 

        visit = set()
        area = 0

        def dfs( r ,c):
            if r < 0 or  c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or (r , c) in visit:
                return 0 
            
            visit.add((r , c))

            return ( 1 + dfs( r + 1 , c) + dfs( r - 1 , c) + dfs( r , c + 1) + dfs( r, c - 1))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r , c) not in visit and grid[r][c] == 1:
                    area = max(area , dfs(r , c))
        return area

        