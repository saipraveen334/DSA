class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1

        for i in range(len(nums)):
            if nums[i] != i:
                res &= nums[i]

        return max(res, 0)