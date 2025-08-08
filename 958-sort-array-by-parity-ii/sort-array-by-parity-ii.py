class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l , r = 0 , 1 

        while l < len(nums) and r < len(nums):

            while l < len(nums) and nums[l] % 2 == 0:
                l += 2

            while r < len(nums) and nums[r] % 2 != 0:
                r += 2 
                
            if l < len(nums) and r < len(nums):
                nums[l] , nums[r] = nums[r] , nums[l]

        return nums
