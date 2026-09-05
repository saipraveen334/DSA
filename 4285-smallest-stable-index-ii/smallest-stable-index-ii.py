class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # get the maximum and minimum at paricular index by prefixMax and prefixMin 

        prefixMax = [0] * len(nums)
        prefixMin = [0] * len(nums)
        prefixMax[0] = nums[0]
        prefixMin[len(nums) - 1] = nums[-1]

        for i in range( 1 , len(nums)):
            prefixMax[i] = max(prefixMax[i - 1] , nums[i])
        
        for i in range(len(nums) - 2, -1, -1):
            prefixMin[i] = min(nums[i] , prefixMin[i + 1])
        
        
        # After setting prefixMax and prefixMins look for the best smallest index 

        for i in range(len(nums)):
            if prefixMax[i] - prefixMin[i] <= k:
                return i 
        return -1 
        