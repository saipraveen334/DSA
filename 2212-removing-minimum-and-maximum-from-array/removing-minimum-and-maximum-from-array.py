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
            return min(
                        minpoint + 1,
                        maxpoint + 1 + len(nums) - minpoint,
                        len(nums) - maxpoint
                      )

        else:
            return min(
                        maxpoint + 1,
                        minpoint + 1 + len(nums) - maxpoint,
                        len(nums) - minpoint
                      )