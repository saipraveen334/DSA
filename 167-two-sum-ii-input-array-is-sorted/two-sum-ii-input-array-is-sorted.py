class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # USING TWO POINTERS

        l = 0 
        r = len(numbers) - 1

        while l < r:
            cursum = numbers[l] + numbers[r]

            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                return [l + 1 , r + 1]


        # USING HASHMAP 
        # seen = defaultdict(int) 

        # for i in range(len(numbers)):
        #     diff = target - numbers[i]

        #     if diff in seen:
        #         return [seen[diff] + 1, i + 1]
            
        #     seen[numbers[i]] = i
        # return []
        
