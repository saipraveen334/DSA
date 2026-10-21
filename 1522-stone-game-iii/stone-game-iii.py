class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        # return (alice - bob) (bob - alice)
        # > 0 -- > alice 
        # < 0 -- > bob 
        # == 0 --> tie

        memo = {}

        def dfs(i):
            # base case
            if i == len(stoneValue):
                return 0 

            if i in memo:
                return memo[i]
            
            res = float("-inf")

            for j in range(i , min(i + 3 , len(stoneValue))):
                res = max(res , sum(stoneValue[i : j + 1]) - dfs(j + 1))
            
            memo[i] = res
            return res
        
        score = dfs(0)
        
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"

        