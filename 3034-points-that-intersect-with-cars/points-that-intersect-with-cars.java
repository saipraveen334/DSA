class Solution {
    public int numberOfPoints(List<List<Integer>> nums) {
        Set <Integer> seen = new HashSet<>();

        for(int i = 0 ; i < nums.size() ; i++)
        {
            int a = nums.get(i).get(0);
            int b = nums.get(i).get(1);

            for( int j= a ; j <= b ; j ++)
            {
                seen.add(j);
            }
        }
        return seen.size();

        
    }
}