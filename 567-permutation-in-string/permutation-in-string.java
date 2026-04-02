import java.util.*;

class Solution {
    public boolean checkInclusion(String s1, String s2) {

        if (s1.length() > s2.length()) return false;

        int[] counts1 = new int[26];
        int[] counts2 = new int[26];
        int matches = 0;
        int l = 0;

        // initial window
        for (int i = 0; i < s1.length(); i++) {
            counts1[s1.charAt(i) - 'a']++;
            counts2[s2.charAt(i) - 'a']++;
        }

        // count initial matches
        for (int i = 0; i < 26; i++) {
            if (counts1[i] == counts2[i]) {
                matches++;
            }
        }

        // sliding window
        for (int r = s1.length(); r < s2.length(); r++) {

            if (matches == 26) return true;

            // ADD RIGHT
            int index = s2.charAt(r) - 'a';
            counts2[index]++;

            if (counts2[index] == counts1[index]) {
                matches++;
            } else if (counts2[index] == counts1[index] + 1) {
                matches--;
            }

            // REMOVE LEFT
            index = s2.charAt(l) - 'a';
            counts2[index]--;

            if (counts2[index] == counts1[index]) {
                matches++;
            } else if (counts2[index] == counts1[index] - 1) {
                matches--;
            }

            l++;
        }

        return matches == 26;
    }
}