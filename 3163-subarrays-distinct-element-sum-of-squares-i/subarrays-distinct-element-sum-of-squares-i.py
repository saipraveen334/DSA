class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            seen = set()

            for j in range(i, n):
                seen.add(nums[j])
                count = len(seen)
                res += count * count

        return res