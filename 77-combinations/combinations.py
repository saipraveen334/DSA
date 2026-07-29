class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i , curSub):
            if i > n :
                if len(curSub) == k: 
                    res.append(curSub.copy())
                return 

            curSub.append(i)
            dfs( i +  1, curSub)

            curSub.pop()
            dfs( i + 1, curSub)



        dfs(1 , [])
        return res 

        