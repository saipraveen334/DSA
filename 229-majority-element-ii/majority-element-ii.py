class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hashmap = {}
        res = []
        for n in nums:
            hashmap[n] = hashmap.get(n , 0) + 1

        for key,value in hashmap.items():

            if value > len(nums) // 3:
                res.append(key)
        return res 
            

        