class Solution:
    def checkValidString(self, s: str) -> bool:

        # GREEDY TECHINIQUE

        leftmax = 0 
        leftmin = 0 

        for c in s: 
            if c == "(":
                leftmax = leftmax + 1
                leftmin = leftmin + 1
            
            if c == ")":
                leftmax = leftmax - 1
                leftmin = leftmin - 1
            
            if c == "*":
                leftmax = leftmax + 1
                leftmin = leftmin - 1

            if leftmax < 0:
                return False
            
            if leftmin < 0:
                leftmin = 0 

        return leftmin == 0

            

        # USING STACK 

        left = []
        star = []

        for i , c in enumerate(s):
            if c == "(":
                left.append(i)

            elif c == "*":
                star.append(i)

            else:
                if not left and not star:
                    return False
                
                if left:
                    left.pop()

                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False

        return len(left) == 0

        # DYNAMIC CACHING 

        dp = [[None] * (len(s) + 1) for _ in range(len(s) + 1 )]


        def dfs(i, total):

            if total < 0:
                return False

            if i == len(s):
                return total == 0


            if dp[i][total] is not None:
                return dp[i][total]
            
            if s[i] == "(":
                res = dfs(i + 1 , total + 1)

            elif s[i] == ")":
                    res = dfs( i + 1 , total - 1)


            else:
                res = dfs( i + 1 , total + 1) or dfs( i + 1, total - 1) or dfs( i + 1, total)

            dp[i][total] = res

            return res

        return dfs(0,0)


