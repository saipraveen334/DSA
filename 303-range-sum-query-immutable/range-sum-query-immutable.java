class NumArray {
    private int[] prefix;

    public NumArray(int[] nums) {
        prefix = new int[nums.length];
        int cur = 0;
        for (int i = 0; i < nums.length; i++) {
            cur += nums[i];
            prefix[i] = cur;
        }
    }

    public int sumRange(int left, int right) {
        int rights = prefix[right];
        int lefts = (left > 0) ? prefix[left - 1] : 0;
        return rights - lefts;
    }
}
