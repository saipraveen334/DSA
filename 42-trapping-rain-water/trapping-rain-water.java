class Solution {
    public int trap(int[] height) {
        if(height == null)
        {
            return 0;
        }
        int l = 0;
        int r = height.length - 1;
        int leftmax = height[l];
        int rightmax = height[r];
        int res =  0;

        while(l < r)
        {
            if (leftmax < rightmax)
            {
                l += 1;
                leftmax = Math.max(leftmax , height[l]);
                res += leftmax - height[l];
            }
            else
            {
                r -= 1;
                rightmax = Math.max(rightmax , height[r]);
                res += rightmax - height[r];
            }
        }
        return res;

        
    }
}