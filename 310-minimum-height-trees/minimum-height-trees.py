class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # best soltion reverse bfs leaves removal method 

        # edge case 
        if n == 1:
            return [0]

        adj = collections.defaultdict(list)
        indegree = [0] * (len(edges) + 1) 

        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)

            indegree[a] += 1
            indegree[b] += 1

        q = collections.deque()

        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        
        remaining = n 

        while remaining > 2:

            size = len(q)
            remaining -= size 

            for _ in range(size):
                node = q.popleft()

                for nei in adj[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 1:
                        q.append(nei)
        return list(q)


        # time limit exceeded solution 


        # edge case 
        if n == 1:
            return [0]

        adj = collections.defaultdict(list)

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def bfs(node , height):

            q = deque()
            visit = set()
            q.append([node , height])
            visit.add(node)

            while q:
                node , h = q.popleft()

                for nei in adj[node]:
                    if nei not in visit:
                        q.append([nei , h + 1])
                        visit.add(nei)

            return h 
        
        res = []
        minheap = []

        for node in range(n):
            minheap.append([bfs(node , 0) , node])
        
        heapq.heapify(minheap)

        hei , node = heapq.heappop(minheap)
        res.append(node)

        while minheap:
            h , n = heapq.heappop(minheap)

            if h == hei:
                res.append(n)
            else:
                break 
        return res 


        






        
            
            
        