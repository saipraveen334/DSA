class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # DFS VERSION 
        adj = collections.defaultdict(list)

        for i , eq in enumerate(equations):
            e1 , e2 = eq
            adj[e1].append([e2 , values[i]])
            adj[e2].append([e1 , 1 / values[i]])

        def dfs(src, target, visited):
            if src not in adj or target not in adj:
                return -1
            if src == target:
                return 1

            visited.add(src)

            for nei, weight in adj[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return weight * result

            return -1

        return [dfs(q[0], q[1], set()) for q in queries]



        # BFS VERSION 

        adj = collections.defaultdict(list)


        for i , eq in enumerate(equations):
            e1 , e2 = eq 

            adj[e1].append([e2 , values[i]]) 
            adj[e2].append([e1 , 1 / values[i]]) # in reverse dir
        
        def bfs(src , target):
            if not src in adj  or not target in adj:
                return -1
            
            q = collections.deque()
            visit = set()

            q.append([src , 1])
            visit.add(src)

            while q:
                node , w = q.popleft()

                # base case 

                if node == target:
                    return w

                for nei , weight  in adj[node]:
                    if nei not in visit:
                        q.append([nei , w * weight])
                        visit.add(nei)
            return -1 
                

        return [bfs(e[0] , e[1]) for e in queries]





        