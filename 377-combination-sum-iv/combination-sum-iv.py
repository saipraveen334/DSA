class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # backtracking + cacheing 
        memo = {}

        def dfs(curSum):
            if curSum >= target:
                if curSum == target:
                    return 1
                else:
                    return 0 
            
            if curSum in memo:
                return memo[curSum]
            
            res = 0 
            
            for n in nums:
                res += dfs(curSum + n)
            
            memo[curSum] = res
            return res
            
        return dfs(0)

        




        # backtracking 

        def dfs(total):
            if total == target:
                return 1
            if total > target:
                return 0

            res = 0
            for num in nums:
                res += dfs(total + num)

            return res

        return dfs(0)