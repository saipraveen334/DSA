class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        maxCount = [1] * len(nums)

        for i in range(len(nums) - 1 , -1 , -1):
            for j in range(i + 1 , len(nums)):

                if nums[i] < nums[j]:
                    maxCount[i] = max(maxCount[i] , maxCount[j] + 1)

        return max(maxCount)


