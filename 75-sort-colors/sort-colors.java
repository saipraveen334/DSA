class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length ;
        int i = 0 ;
        int left = 0 , right = n -1 ;

        while (i <= right)
        {
            if (nums[i] == 0)
            {
                int temp = nums[i] ;
                nums[i] = nums[left] ;
                nums[left] = temp ; 
                left++ ;
                i++ ;
            }
            else if (nums[i] == 2)
            {
                int temp1 = nums[i] ;
                nums[i] = nums[right] ;
                nums[right] = temp1 ;
                right -- ;
            }
            else
            {
                i ++ ;
            }
        }
        
    }
}