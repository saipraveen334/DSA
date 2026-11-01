class Solution:
    def minMoves(self, nums: list[int]) -> int:
        k = min(nums)
        total = 0

        for n in nums:
            total += (n - k)
        return total 
        