class Solution {
    public int largestRectangleArea(int[] heights) {
        // STACK WITH INDEX -- > HEIGHT 
        // MONOTONICALLY INCREASING STACK

        Stack<int[]> stack = new Stack<>();
        int maxArea = 0;

        for(int i = 0 ; i < heights.length ; i++)
        {
            int h1 = heights[i];
            int start = i ;

            while(!stack.isEmpty() && stack.peek()[1] >= h1)
            {
                int pair[] = stack.pop();
                int ph = pair[1] ;
                int idx = pair[0] ;

                maxArea = Math.max(maxArea , ph * (i - idx));
                start = idx ;
            }
            stack.push(new int[] {start , h1});
        } 

        while(!stack.isEmpty())
        {
            int pair[] = stack.pop();
            int idx = pair[0];
            int height = pair[1];

            maxArea = Math.max(maxArea , height * (heights.length - idx));
        }
        return maxArea;

        
    }
}