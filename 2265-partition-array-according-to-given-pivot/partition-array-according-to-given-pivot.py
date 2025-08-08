class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l , left = 0 , 0
        r , right = len(nums) - 1 , len(nums) - 1
        res = [0] * len(nums)

        while l < len(nums):
            if nums[l] < pivot:
                res[left] = nums[l]
                left += 1
            if nums[r] > pivot:
                res[right] = nums[r]
                right -= 1
            l += 1
            r -= 1
        while left <= right:
            res[left] = pivot
            left += 1

        return res 


        