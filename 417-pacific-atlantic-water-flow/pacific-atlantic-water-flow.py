class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacSet = set()
        altSet = set()
        res = []

        # dfs main function 
        # water level should increase from edges to middle & viceverse 

        def dfs(r , c , visit , prevHeight):

            if r < 0 or c < 0 or r == len(heights) or c == len(heights[0]) or (r , c) in visit or heights[r][c] < prevHeight:
                return 
            
            visit.add((r ,c))

            dfs( r + 1 , c , visit , heights[r][c])
            dfs( r - 1 , c , visit , heights[r][c])
            dfs( r , c - 1 , visit , heights[r][c])
            dfs( r , c + 1 , visit , heights[r][c])


        for c in range(len(heights[0])):
            dfs(0 , c , pacSet , heights[0][c])
            dfs(len(heights) - 1 , c , altSet , heights[len(heights)- 1][c])
        
        for r in range(len(heights)):
            dfs(r , 0 , pacSet , heights[r][0])
            dfs(r , len(heights[0]) - 1 , altSet , heights[r][len(heights[0]) - 1])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r , c ) in pacSet and ( r, c ) in altSet:
                    res.append([r , c])
        
        return res

                    




        