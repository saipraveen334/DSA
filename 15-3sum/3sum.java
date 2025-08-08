class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int threesum = 0;
        Arrays.sort(nums);

        for (int i = 0 ; i < nums.length - 2 ; i++)
        {
            if (i > 0 && nums[i-1] == nums[i])
            {
                continue;
            }
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right)
            {
                threesum = nums[i] + nums[left] + nums[right];

                if (threesum < 0)
                {
                    left ++ ;
                }
                else if (threesum > 0)
                {
                    right --;
                }
                else
                {
                    res.add(Arrays.asList(nums[i] , nums[left] , nums[right]));

                    // REMOVING DULICATES
                    while (left < right && nums[left] == nums[left + 1]){
                        left ++ ;
                    }
                    while (left < right && nums[right] == nums[right - 1]){
                        right -- ;
                    }
                    left ++ ;
                    right --;


                }
            }
        }
        return res;

        
    }
}