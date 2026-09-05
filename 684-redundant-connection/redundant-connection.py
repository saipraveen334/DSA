class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # topological sort 
        adj = [[] for _ in range(len(edges) + 1)]

        indegree = [0] * (len(edges) + 1) 
        for u , v in edges:
            adj[v].append(u)
            adj[u].append(v)

            indegree[u] += 1
            indegree[v] += 1
        
        # add the node to queue that has one degree because its a leaf , not a part of cycle 

        q = collections.deque()
        
        for i in range( 1 , len(edges) + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()

            indegree[node] -= 1

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 1:
                    q.append(nei)

        # reversed becuase probably the last edge added to cycle to be removed 
        for u , v in reversed(edges):
            if indegree[u] == 2 and indegree[v] != 0:
                return[u , v]

















        # dfs appraoch also
        # checking if we can reach the edge before adding it 

        adj = [[] for _ in range(len(edges) + 1)]

        def dfs(node , target , visit):

            # reached base case 

            if node == target:
                return True 
            
            visit[node] = True 

            for nei in adj[node]:
                if not visit[nei]:
                    if dfs( nei , target , visit):
                        return True 
            
            return False 
                    



        for n1 , n2 in edges:

            visit = [False] * (len(edges) + 1)

            if dfs(n1 , n2 , visit):
                return [n1 , n2]

            # we cant reach the edge so add it 

            adj[n1].append(n2)
            adj[n2].append(n1)
        
        return [] # no cycle 



        # union find
        N = len(edges)

        par = [i for i in range(N + 1)]

        rank = [1] * (N + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p


        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)

            if p1 == p2:
                return False 
            
            elif rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            
            else:
                rank[p2] += rank[p1]
                par[p1] = p2

            return True 
        
        for n1 , n2 in edges:
            if not union(n1 , n2):
                return [n1 , n2]
        
            
            