class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)
        perm = []


        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            
            for num in counter:
                if counter[num] > 0:
                    perm.append(num)
                    counter[num] -= 1

                    dfs()

                    perm.pop()
                    counter[num] += 1
        dfs()
        return res
        