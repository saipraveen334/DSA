class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7 
        bits = [0] * 32
        res = 0

        # counting the 1's bits of numbers
        for n in nums:
            for b in range(32):
                if n & (1 << b):
                    bits[b] += 1
        
        for _ in range(k):
            num = 0 

            for b in range(32):
                if bits[b] > 0:
                    num = num | (1 << b) # setting the bit

                    bits[b] -= 1

            res = (res + num * num) % mod
        return res

        