class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i , curSub):
            if i >= len(nums):
                res.append(curSub.copy())
                return 
            
            curSub.append(nums[i])
            dfs( i + 1 , curSub)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            curSub.pop()
            dfs( i  + 1 , curSub)
        dfs(0 , [])
        return res
        