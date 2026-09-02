class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        # edge case 
        if len(nums) == 1:
            return 1
        
        # get the index of the maximum number 

        maxpoint = 0 

        for i in range(len(nums)):
            if nums[i] > nums[maxpoint]:
                maxpoint = i 
        
        # get the index of the minimum number 

        minpoint = 0 

        for i in range(len(nums)):
            if nums[i] < nums[minpoint]:
                minpoint = i
            
        if maxpoint < minpoint:

            return min(len(nums[:minpoint + 1]) ,
                       len(nums[:maxpoint + 1] + nums[minpoint:]) ,
                       len(nums[maxpoint:]))
        else:

            return min(len(nums[: maxpoint + 1]),
                       len(nums[:minpoint + 1] + nums[maxpoint:]),
                       len(nums[minpoint:]))
        
