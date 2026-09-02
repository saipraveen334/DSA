class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # base cases
        if len(nums) == 1:
            return 1

        # get the indexes of maximum and minimum respectively
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                l += 1
            elif nums[r] < nums[l]:
                r -= 1
            else:
                break

        maxpoint = l

        # get min point
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] > nums[r]:
                l += 1
            elif nums[r] > nums[l]:
                r -= 1
            else:
                break

        minpoint = l

        # get the indexes
        if maxpoint < minpoint:
            return min(
                maxpoint + 1 + len(nums) - minpoint,
                minpoint + 1,
                len(nums) - maxpoint
            )
        else:
            return min(
                minpoint + 1 + len(nums) - maxpoint,
                maxpoint + 1,
                len(nums) - minpoint
            )