class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i , curSub , total):
            if total == target:
                res.append(curSub.copy())
                return 
            
            #BASE CONDITION 
            if total > target or i >= len(candidates):
                return 
            
            curSub.append(candidates[i])
            dfs(i + 1, curSub , total + candidates[i])

            curSub.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, curSub , total)
            
        dfs( 0 , [] , 0)
        return res


            

            
        