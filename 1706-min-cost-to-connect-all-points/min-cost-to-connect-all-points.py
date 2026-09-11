class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = {i : [] for i in range(N)}

        for i in range(N):
            x1 , x2 = points[i]

            for j in range(i + 1, N):
                y1 , y2 = points[j]

                absDis = abs(x1 - y1) + abs(x2 - y2)

                adj[i].append([absDis , j])
                adj[j].append([absDis , i])
        
        minheap = [[0 , 0]]
        res = 0 
        visit = set()

        while len(visit) < N:
            cost , point = heapq.heappop(minheap)

            if point in visit:
                continue 

            res += cost 
            visit.add(point)

            for neiCost , nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minheap , [neiCost , nei])
                
        return res
            




        