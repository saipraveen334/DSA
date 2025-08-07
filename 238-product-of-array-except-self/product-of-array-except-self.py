class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Res = [0] * len(nums)

        Prefix = 1 

        for i in range(len(nums)):
            Res[i] = Prefix
            Prefix = Prefix * nums[i]

        Postfix = 1 

        for i in range(len(nums)- 1 , -1 , -1 ):
            Res[i] = Res[i] * Postfix
            Postfix = Postfix * nums[i]
        
        return Res
    

        