class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # COUNT THE FRESH ORANGES
        # BFS 
        
        q = collections.deque()
        fresh = 0 
        time = 0 
        directions =[[0 ,1] , [1,0] , [0 , -1] , [-1 , 0]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1

                # adding the rotten oranges to the queue 

                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r , c = q.popleft()

                for nr , nc in directions:
                    row = nr + r
                    col = nc + c

                    # out of bounds condition 

                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row , col))
                        fresh -= 1
                    else:
                        continue
            time += 1
        
        return time if fresh == 0 else -1
                


        