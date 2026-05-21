class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;

        int pair[][] = new int[n][2];

        for(int i = 0 ; i < n ; i++)
        {
            pair[i][0] = position[i];
            pair[i][1] = speed[i];
            
        }

        Arrays.sort(pair , (a , b) -> b[0] - a[0]);

        Stack<Double> stack = new Stack<>();

        for(int[] car : pair)
        {
            int p = car[0];
            int s = car[1];

            stack.push((double)(target - p) / s);

            while(stack.size() > 1 && stack.get(stack.size() - 2) >= stack.peek())
            {
                stack.pop();
            }
        }
        return stack.size();


        
    }
}