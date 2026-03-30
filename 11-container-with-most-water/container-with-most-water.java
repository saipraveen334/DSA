class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int resmax = 0;

        while(l < r)
        {
            int hmax = Math.min( height[l] , height[r]);
            resmax = Math.max(resmax , hmax * (r - l));

            if(height[l] > height[r])
            {
                r -= 1;
            }
            else
            {
                l += 1;
            }


        }
        return resmax;
        
    }
}