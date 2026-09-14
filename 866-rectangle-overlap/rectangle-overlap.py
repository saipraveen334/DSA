class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a1, b1, c1, d1 = rec1
        a2, b2, c2, d2 = rec2

        return max(a1, a2) < min(c1, c2) and max(b1, b2) < min(d1, d2)