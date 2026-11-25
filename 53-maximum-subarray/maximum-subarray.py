class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cursum = 0 
        maxVal = nums[0]

        for n in nums:
            if cursum < 0:
                cursum = 0 
            cursum += n 
            maxVal = max(maxVal , cursum)
        return maxVal