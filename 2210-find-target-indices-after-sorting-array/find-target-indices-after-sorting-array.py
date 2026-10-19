class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                l = i + 1

                while l < len(nums) and nums[l] == target:
                    res.append(l)
                    l += 1
                
                break 
        return res