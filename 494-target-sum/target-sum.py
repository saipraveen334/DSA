class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # backtracking + caching

        memo = {}

        def dfs(i , total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i , total) in memo:
                return memo[(i , total)]
            
            memo[(i , total)] = dfs(i + 1 , total - nums[i]) + dfs (i + 1, total + nums[i])

            return memo[(i , total)]

        return dfs(0 , 0)





        # backtracking 

        def dfs(i , total):
            if i == len(nums):
                if target == total:
                    return 1
                else:
                    return 0
            
            return dfs(i + 1 , - nums[i] + total) + dfs(i + 1 , nums[i] + total)

        return dfs(0 , 0)

        