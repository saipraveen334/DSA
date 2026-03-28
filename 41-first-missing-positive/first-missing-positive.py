class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0 
        
        for i in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val < len(nums) + 1:
                if nums[val -1] < 0:
                    continue 
                elif nums[val - 1] > 0:
                    nums[val - 1] *= -1 
                else:
                    nums[val - 1] = -11 * (len(nums) + 1)

        for i in range(1 , len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1

                    