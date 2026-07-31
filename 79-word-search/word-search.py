class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(r , c , i):
            if i == len(word):
                return True 
            
            if r >= rows or c >= cols or r < 0 or c < 0 or board[r][c] != word[i] or (r,c) in visit:
                return False 
            
            visit.add((r,c))

            res = (dfs(r , c + 1 , i + 1) or 
            dfs(r , c - 1 , i + 1) or 
            dfs(r + 1 , c , i + 1) or 
            dfs(r - 1 , c , i + 1))

            visit.remove((r,c))

            return res
            


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r , c , 0):
                    return True 
        
        return False
        