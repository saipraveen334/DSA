class Solution:
    def climbStairs(self, n: int) -> int:

        # brute force with caching 

        cache = [-1] * n 

        def dfs(i):
            # base case 
            if i >= n:
                return i == n 
            
            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)

            return cache[i]

        return dfs(0)

        # time limit exceeded brute force 

        def dfs(i):
            #base case

            if i >= n:
                return i == n 
            
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)
        