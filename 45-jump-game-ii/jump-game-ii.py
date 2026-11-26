class Solution:
    def jump(self, nums: list[int]) -> int:
        # greedy sol
        l = 0 
        r = 0 
        res = 0

        while r < len(nums) - 1:
            far = 0

            for j in range(l , r + 1):
                far = max(far , j + nums[j])

            l = r + 1
            r = far 
            res += 1
        return res


        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            
            if i in memo:
                return memo[i]

            res = float("inf")

            for j in range(1 , nums[i] + 1):
                res = min(res , 1 + dfs(i + j))

            memo[i] = res
            return res
        
        return dfs(0)