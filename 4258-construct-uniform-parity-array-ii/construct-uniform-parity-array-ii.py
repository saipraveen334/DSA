class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        if all( x % 2 == 0 for x in nums1):
            return True 
        
        if all( x % 2 != 0 for x in nums1):
            return True 

        minEven = minOdd = float("INF")
        for n in nums1:
            if n % 2 == 0:
                minEven = min(minEven , n)
            else:
                minOdd = min(minOdd , n) 
        
        return minEven > minOdd

        