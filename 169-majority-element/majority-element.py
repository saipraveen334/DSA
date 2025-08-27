class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}
        maxc = 0
        ans = 0

        for n in nums:
            count[n] = count.get(n,0) + 1

            ans = n if count[n] > maxc else ans
            maxc = max(maxc , count[n])
        return ans
        
        