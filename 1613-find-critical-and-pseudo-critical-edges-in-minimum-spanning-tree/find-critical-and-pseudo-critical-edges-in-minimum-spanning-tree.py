class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n 
    
    def find(self , x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self , n1 ,n2):

        # finding parents 
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False 
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        
        else:
            self.par[p1] = p2 
            self.rank[p2] += self.rank[p1]
        return True 

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        for i , e in enumerate(edges):
            # original index 
            e.append(i)

        edges.sort(key = lambda  x : x[2])
        uf = UnionFind(n)

        mst_weight = 0 

        for v1 , v2 , w , i in edges:
            if uf.union(v1 , v2):
                mst_weight += w
        
        criticalEdges = []
        pseudoEdges = []

        for n1 , n2 , wei , i in edges:

            # try to form a minimum spanning tree without the cur edge , if it is unable to form then it is crtical edge 

            cur_weight = 0
            uf = UnionFind(n)

            for v1 , v2 , w , j in edges:
                if i != j and uf.union(v1 ,v2):
                    cur_weight += w
            
            if cur_weight > mst_weight or max(uf.rank) != n:
                criticalEdges.append(i)
                continue #because no edge is pseudo critical if it is a critical edge
             
            # hence it is not critical edge , a edge is said to be a pseudo critical if it can form mst by forcefully including itself in 

            uf = UnionFind(n)
            uf.union(n1 , n2)
            cur_weight = wei

            for v1 , v2 , w , j in edges:
                if uf.union(v1 , v2):
                    cur_weight += w

            # can form forcefully a mst so , pseduo critical edge 
            if cur_weight == mst_weight: 
                pseudoEdges.append(i)
        
        return[criticalEdges , pseudoEdges]











        