from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # dijstra (minheap) with state 

        # creating a adjacency list 
        adj = defaultdict(list)

        for u , v , w in edges:
            adj[u].append((v , w))
        
        

        dist = [[float("inf")] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        minheap = [(0 , 0 , 1)]  # cost , node , count

        while minheap:
            cost , u , count = heapq.heappop(minheap)

            if cost > dist[u][count]:
                continue 
            
            # base case 
            if u == n - 1:
                return cost 

            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k:
                    new_cost = cost + w

                    if new_cost < dist[v][new_count]:
                        dist[v][new_count] = new_cost
                        heapq.heappush(minheap, (new_cost, v, new_count))
        return -1
