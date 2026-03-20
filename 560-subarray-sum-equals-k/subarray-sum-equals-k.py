class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = { 0 : 1 }
        res = 0
        total = 0

        for n in nums:
            total += n
            diff = total - k

            if diff in prefix:
                res += prefix[diff]

            prefix[total] = 1 + prefix.get(total , 0)
        return res
        



        