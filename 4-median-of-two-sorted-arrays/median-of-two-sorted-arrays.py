class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 
        B = nums2 
        total = len(A) + len(B)

        half = total // 2

        if len(A) > len(B):
            A , B = B , A

        l = 0 
        r = len(A) - 1

        while True:
            m = (r+l) // 2

            m1 = half - m - 2

            Aleft = A[m] if m >= 0 else float("-inf")
            Bleft = B[m1] if m1 >= 0 else float("-inf")
            Aright = A[m + 1] if (m + 1) < len(A) else float("inf")
            Bright = B[m1 + 1] if (m1 + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Aright , Bright)
                return (min(Aright , Bright) + max( Aleft , Bleft)) / 2
            if Aleft > Bright:
                r = m - 1
            else:
                l = m + 1





        