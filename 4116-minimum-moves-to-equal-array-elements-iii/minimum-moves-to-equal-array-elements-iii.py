class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        res = 0

        for n in nums:
            res += maxi - n

        return res