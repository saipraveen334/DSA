class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet <Integer> HS = new HashSet<>();

        for (int n : nums) {
            if (HS.contains(n)) {
                return true;
            }
            HS.add(n);
        }
        return false;
        
    }
}