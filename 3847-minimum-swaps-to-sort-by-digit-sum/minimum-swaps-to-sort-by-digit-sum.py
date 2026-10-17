class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitsum(n):
            total = 0 

            while n > 0:
                rem = n % 10 
                total += rem 
                n = n // 10
            
            return total 
        
        target = sorted(nums , key = lambda x :(digitsum(x) , x))
        pos = {x : i  for i , x in enumerate(target)}

        swapCnt = 0 

        for i in range(len(nums)):

            while nums[i] != target[i]:
                j = pos[nums[i]]

                nums[i] , nums[j] = nums[j] , nums[i]
                swapCnt += 1

        return swapCnt


        