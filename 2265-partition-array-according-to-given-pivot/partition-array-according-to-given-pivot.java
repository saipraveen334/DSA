class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length ;
        int l = 0 , r = n - 1 ;
        int left = 0 , right = n - 1;
        int[] res = new int[n];
        while (l < n) 
        {
            if (nums[l] < pivot)
            {
                res[left] = nums[l] ;
                left++ ;
            }
            if (nums[r] > pivot)
            {
                res[right] = nums[r] ;
                right-- ;
            }
            l++ ;
            r --;
        }
        while( left <= right )
        {
            res[left] = pivot ;
            res[right] = pivot ;
            left ++ ;
            right -- ;
        }
        return res;
        
    }
}