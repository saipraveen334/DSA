class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        base = 10
        mod = 10 ** 9 + 7 # to handle large i/o 

        power = [1] * (len(nums) + 1) 
        pre = [0] * (len(nums) + 1)

        # storing the powers and prefix values
        for i in range(len(nums)):
            power[i + 1] = (power[i] * base) % mod

            # adding 1 to avoid zeros 
            pre[i + 1] = (pre[i] * base + nums[i] + 1) % mod

        # hash function 
        def getHash(l , r):
            return (pre[r] - pre[l] * power[r - l]) % mod
        
        # check the given length respectively 
        def check(k):

            # to get the all the subarray counts with k length 
            freq = {}

            for i in range(len(nums) - k + 1):
                h = getHash(i , i + k)
                freq[h] = 1 + freq.get(h , 0)
            
            for count in freq.values():
                if count == 1:
                    return True 
            
            return False 
        
        l = 1 
        r = len(nums)

        res = len(nums) 

        while l <= r:
            m = (r + l) // 2

            if check(m): 
                res = m 
                r = m - 1
            else:
                l = m + 1
        return res





        




        