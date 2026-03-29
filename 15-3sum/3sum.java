class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // using pointers
        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList<>();

        for(int i = 0 ; i < nums.length ; i++)
        {
            if(nums[i] > 0)
            {
                break;
            }
            if(i > 0 && nums[i] == nums[i-1])
            {
                continue;
            }
            int l = i + 1;
            int r = nums.length - 1;
            int cursum = 0;

            while(l < r)
            {
                cursum = nums[i] + nums[l] + nums[r];

                if(cursum > 0)
                {
                    r -= 1;
                }
                else if(cursum < 0)
                {
                    l += 1;
                }
                else
                {
                    res.add(Arrays.asList(nums[i] , nums[l] , nums[r]));
                    l += 1;
                    r -= 1;

                    while(nums[l] == nums[l-1] && l < r)
                    {
                        l += 1;
                    }
                }
            }
        }
        return res;

        
    }
}