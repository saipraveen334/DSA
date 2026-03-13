class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} # val -> index

        for i , num in enumerate(nums):
            diff = target - num 

            if diff in prevmap:
                return [prevmap[diff] , i]
            prevmap[num] = i
            


        