class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int l = 0;

        HashSet<Integer> window = new HashSet<>();

        for( int r = 0 ; r < nums.length ; r++)
        {
            if( r - l > k)
            {
                window.remove(nums[l]);
                l += 1;
            }
            if (window.contains(nums[r]))
            {
                return true;
            }
            window.add(nums[r]);
        }

        return false;
    }
}