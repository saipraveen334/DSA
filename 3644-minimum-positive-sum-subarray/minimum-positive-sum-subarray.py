class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = float("inf")
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(n):
            for k in range(l , r + 1):
                j = i + k

                if j > n:
                    break 
                
                total = prefix[j] - prefix[i]

                if total > 0:
                    res = min(res , total)
        return res if res != float("inf") else -1 

        

        