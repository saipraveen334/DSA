class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l , left = 0 , 0
        r , right = len(nums) - 1 , len(nums) - 1
        res = [0] * len(nums)

        for l in range(len(nums)):
            if nums[l] < pivot:
                res[left] = nums[l]
                left += 1
        for r in range(len(nums) - 1 , -1 ,-1):
            if nums[r] > pivot:
                res[right] = nums[r]
                right -= 1
        for k in range(left , right + 1):
            res[k] = pivot
        return res


        