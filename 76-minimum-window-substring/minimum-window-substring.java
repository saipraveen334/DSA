class Solution {
    public String minWindow(String s, String t) {

        //INITAIL EDGE CASE 

        if(s.length() < t.length())
        {
            return "";
        }

        HashMap<Character , Integer> countT = new HashMap<>();
        HashMap<Character , Integer> window = new HashMap<>();

        for(int i = 0; i < t.length() ; i++)
        {
            char ch = t.charAt(i);
            countT.put(ch , countT.getOrDefault(ch , 0) + 1);
        }

        String res = "";
        int reslen = Integer.MAX_VALUE;
        int l = 0;
        int need = countT.size();
        int have = 0;

        for(int r = 0 ; r < s.length(); r++)
        {
            char c = s.charAt(r);
            window.put(c , window.getOrDefault(c , 0) + 1);

            if(countT.containsKey(c) && countT.get(c).equals(window.get(c)))
            {
                have++;
            }

            while(have == need)
            {
                if((r - l + 1) < reslen)
                {
                    reslen = r - l + 1;
                    res = s.substring(l , r + 1);

                }
                char ch = s.charAt(l);
                window.put(ch , window.get(ch) - 1);

                if(countT.containsKey(ch) && countT.get(ch) > window.get(ch))
                {
                    have--;
                }

                l++;
            }

        }
        return res;

        
    }
}