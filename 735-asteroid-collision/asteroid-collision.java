class Solution {
    public int[] asteroidCollision(int[] asteroids) {

        Stack<Integer> stack = new Stack<>();

        for(int n : asteroids)
        {
            boolean flag = true;

            while(!stack.isEmpty() && n < 0 & stack.peek() > 0) 
            {
                
                int res = stack.peek() + n ;

                if( res > 0)
                {
                    flag = false;
                    break;

                }
                else if( res == 0)
                {
                    flag = false;
                    stack.pop();
                    break;
                }
                else
                {
                    stack.pop();
                    continue;
                }


            }
            if(flag)
            {
                stack.push(n);
            }
        }
        int ans[] = new int[stack.size()];

        int i = stack.size() - 1; 
        
        while(!stack.isEmpty())
        {
            ans[i--] = stack.pop(); 
        }

        return ans;
        
    }
}