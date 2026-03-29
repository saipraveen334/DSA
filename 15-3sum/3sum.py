class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i , n in enumerate(nums):

            if n > 0:
                break 
            
            if i > 0 and nums[i - 1] == n:
                continue 
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                cursum = n + nums[l] + nums[r]

                if cursum > 0:
                    r -= 1

                elif cursum < 0:
                    l += 1
                
                else:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l += 1 
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

                    
