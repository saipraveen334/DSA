class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        minheap = [[grid[0][0] , 0 , 0]]
        visit = set()
        visit.add((0 , 0))
        directions = [[0 , 1 ] , [1 , 0] , [- 1, 0] , [0 , -1]]

        while minheap:
            t , r , c = heapq.heappop(minheap)

            # final case 

            if r == rows -1 and c == cols - 1:
                return t 
            
            for dr , dc in directions:
                nr = dr + r
                nc = dc + c

                # out of bounds or in already visited

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr , nc) in visit:
                    continue 
                
                visit.add((nr , nc))

                maxVal = max(t , grid[nr][nc])

                heapq.heappush(minheap , [maxVal , nr , nc])
        return 0






        

        