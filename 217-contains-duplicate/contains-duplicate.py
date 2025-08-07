class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        HashSet = set()

        for n in nums:
            if n in HashSet:
                return True 
            HashSet.add(n)
        return False

        