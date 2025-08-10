class Solution {
    public String reverseWords(String s) {
        Deque<String> q = new ArrayDeque<>();

        int start = -1 ;
        int i = 0 ;

        while (i < s.length())
        {
            if (s.charAt(i) != ' ')
            {
                start = i ;

                while (i < s.length() && s.charAt(i) != ' ')
                {
                    i++ ;
                }

                q.addFirst(s.substring(start , i)) ;
                i--;

            }
            i++ ;
        }
        return String.join(" ",q) ;
        
    }
}