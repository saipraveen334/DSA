class Solution:
    def maxArea(self, height: List[int]) -> int:

        rightmax = len(height) - 1
        leftmax = 0 
        maxres = 0

        while leftmax < rightmax:
            hmax = min(height[leftmax] , height[rightmax])

            maxres = max(maxres , (rightmax - leftmax) * hmax)

            if height[leftmax] <= height[rightmax]:
                leftmax += 1
            else:
                rightmax -= 1
        return maxres
        