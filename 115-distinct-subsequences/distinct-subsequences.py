class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # cacheing + dfs to avoid time limit exceeded

        dp = {}
        res = 0

        def dfs(i , j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0 
            
            if (i , j) in dp:
                return dp[(i, j)]
            
            # not macthing the current charcter or trying the possible combinations 

            res = dfs( i + 1 , j)

            if s[i] == t[j]:
                res += dfs( i + 1 , j + 1)
            
            dp[(i , j)] = res

            return res

        return dfs(0, 0)



        # time limit exceeded dfs 

        res = 0

        if len(t) > len(s):
            return 0 


        def dfs(i , j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            # skip the charcter to find is there more possibilites or dont match the current character 
            res = dfs(i + 1 , j)

            if s[i] == t[j]:
                res += dfs(i + 1 , j + 1)
            
            return res

        return dfs(0 , 0)
        