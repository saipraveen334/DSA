class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posdia = set()
        negdia = set()

        res = 0

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return 
            
            for c in range(n):
                if c in col or (r + c) in posdia or (r - c) in negdia:
                    continue

                col.add(c)
                posdia.add(r + c)
                negdia.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                posdia.remove(r + c)
                negdia.remove(r - c)

        backtrack(0)

        return res

                
                

        