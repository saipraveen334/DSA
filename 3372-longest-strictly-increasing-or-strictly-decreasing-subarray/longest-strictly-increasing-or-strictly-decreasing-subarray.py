class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # strcitly increasing 
        l = 0
        res1 = 0
        
        while l < len(nums):
            leng = 1
            while l + 1 < len(nums) and nums[l] < nums[l + 1]:
                leng += 1
                l += 1
            res1 = max(res1 , leng)
            l += 1
        
        # strictly decreasing 
        res2 = 0 
        r = len(nums) - 1 

        while r > 0:
            leng = 1
            while r - 1 >= 0 and nums[r] < nums[r - 1]:
                leng += 1
                r -= 1
            res2 = max(res2 , leng)
            r -= 1

        return max(res1 , res2)