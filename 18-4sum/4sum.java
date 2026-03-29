class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList<>();

        for(int i = 0 ; i < nums.length ; i++)
        {
            if( i > 0 && nums[i] == nums[i - 1])
            {
                continue;
            }
            for(int j = i + 1 ;j < nums.length ; j++)
            {
                if( j > i + 1 && nums[j] == nums[j - 1])
                {
                    continue;
                }
                int l = j + 1 ;
                int r = nums.length - 1 ;


                while( l < r )
                {
                    long foursum = (long)nums[l] + nums[r] + nums[i] + nums[j];

                    if(foursum > target)
                    {
                        r -= 1;
                    }
                    else if(foursum < target)
                    {
                        l += 1;
                    }
                    else
                    {
                        res.add(Arrays.asList(nums[i] , nums[j] , nums[l] , nums[r]));
                        l += 1;
                        r -= 1;

                        while( l < r && nums[l] == nums[l - 1])
                        {
                            l += 1;
                        }

                        while(l < r && nums[r + 1] == nums[r])
                        {
                            r -= 1; 
                        }

                    }
                }
            }
        }
        return res;
        
    }
}