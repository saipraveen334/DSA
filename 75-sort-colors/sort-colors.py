class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0 
        r = len(nums) - 1
        i = 0

        while l <= r:

            if nums[l] == 0:
                nums[l] , nums[i] = nums[i] , nums[l]
                i += 1
                l += 1

            elif nums[l] == 2:
                nums[l] , nums[r] = nums[r] , nums[l]
                r -= 1
            
            else:
                l += 1



            
        