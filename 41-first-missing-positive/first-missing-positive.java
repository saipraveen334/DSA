class Solution {
    public int firstMissingPositive(int[] nums) {

        for(int i = 0 ; i < nums.length ; i++)
        {
            if(nums[i] < 0)
            {
                nums[i] = 0;
            }
        }
        int val = -1 * (nums.length + 1);

        for(int ind = 0 ; ind < nums.length ; ind++)
        {
            val = Math.abs(nums[ind]);

            if( 1 <= val &&  val <= nums.length)
            {
                if (nums[val - 1] < 0) 
                {
                    continue;
                } 
                else if( nums[val - 1] > 0)
                {
                    nums[val - 1] *= -1;
                }
                else
                {
                    nums[val - 1] = -1 * (nums.length + 1);
                }

            }

        }

        for( int j = 1 ; j < nums.length + 1 ; j++)
        {
            if( nums[j - 1] >= 0)
            {
                return j;
            }


        }
        return nums.length + 1;

        
    }
}