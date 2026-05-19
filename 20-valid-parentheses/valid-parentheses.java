class Solution {
    public boolean isValid(String s) {
        HashMap<Character , Character> hs = new HashMap<>();
        hs.put(')' , '(');
        hs.put('}' , '{');
        hs.put(']' , '[' );

        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray())
        {
            if(hs.containsKey(c))
            {
                if(!stack.isEmpty() && stack.peek() == hs.get(c))
                {
                    stack.pop();
                }
                else
                {
                    return false;
                }
            }
            else
            {
                stack.push(c);

            }
        }

        return stack.isEmpty();
        
    }
}