class Solution {
    public int characterReplacement(String s, int k) {
        int maxf = 0;

        HashMap<Character , Integer > window = new HashMap<>();

        int res = 0;
        int l = 0;

        for(int r = 0 ; r < s.length() ; r++)
        {
            char c = s.charAt(r);

            window.put(c , window.getOrDefault(c , 0) + 1);

            maxf = Math.max(maxf , window.get(c));

            while((r - l + 1) - maxf > k)
            {
                char leftch = s.charAt(l);
                window.put(leftch , window.get(leftch) - 1);
                l++;
            } 

            res = Math.max(res , (r - l + 1));

        }
        return res;

        
    }
}