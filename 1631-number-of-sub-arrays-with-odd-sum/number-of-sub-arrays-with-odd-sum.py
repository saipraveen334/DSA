class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        evnCnt = 0
        oddCnt = 0
        res = 0 
        curSum = 0 
        MOD = 10 ** 9 + 7

        for n in arr:
            curSum += n 
            if curSum % 2 == 0:
                res = (res + oddCnt) % MOD
                evnCnt += 1
            else:
                res = (res + 1 + evnCnt) % MOD
                oddCnt += 1
        return res % MOD

        