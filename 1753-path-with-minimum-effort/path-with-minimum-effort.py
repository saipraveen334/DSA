class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        # dijkstra algo

        minheap = [[0, 0 , 0]] #( absolute diff , r , c )

        heapq.heapify(minheap)

        visit = set()

        rows = len(heights)
        cols = len(heights[0])

        directions = [[0 , 1] , [0 , - 1] , [1 , 0] , [-1 , 0]]

        while minheap:
            absDif , r , c = heapq.heappop(minheap)

            if (r , c) in visit:
                continue

            visit.add((r , c)) 

            # base case 
            if r == rows - 1 and c == cols - 1:
                return absDif 
            
            
            for dr , dc in directions:
                nr = dr + r
                nc = dc + c

                # out of bounds and visit

                if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr , nc) in visit:
                    continue 

                newDif = max(absDif , abs(heights[nr][nc] - heights[r][c]))

                heapq.heappush(minheap , [newDif , nr , nc])
        return 0








        