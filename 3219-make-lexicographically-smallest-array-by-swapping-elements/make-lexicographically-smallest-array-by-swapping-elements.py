class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        group = []
        numGroup = {}
         
        for n in sorted(nums):
            if not group or abs(n - group[-1][-1]) > limit:
                group.append(deque())
            
            group[-1].append(n)
            numGroup[n] = len(group) - 1
        
        res = []

        for n in nums:
            # get the group --> j 

            j = numGroup[n]
            res.append(group[j].popleft())

        return res


        