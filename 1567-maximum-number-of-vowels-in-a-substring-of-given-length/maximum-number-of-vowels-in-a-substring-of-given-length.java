class Solution {
    public int maxVowels(String s, int k) {
        HashSet<Character> vowels = new HashSet<>(Arrays.asList('a' , 'e' , 'i' , 'o' , 'u')) ;
        int count = 0 , maxc = 0 , l = 0;

        for( int r = 0 ; r< s.length() ; r++)
        {
            if (vowels.contains(s.charAt(r)))
            {
                count ++ ;
            }
            if ((r - l + 1) > k)
            {
                if (vowels.contains(s.charAt(l)))
                {
                    count --;
                }
                l++ ;
            }
            maxc = Math.max(maxc , count) ;
        } 
        return maxc ;
        
    }
}