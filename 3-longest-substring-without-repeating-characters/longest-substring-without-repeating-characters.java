import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {

        int l = 0;
        int res = 0;

        HashSet<Character> window = new HashSet<>();

        for (int r = 0; r < s.length(); r++) {

            while (window.contains(s.charAt(r))) {
                window.remove(s.charAt(l));
                l++;
            }

            window.add(s.charAt(r));
            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}