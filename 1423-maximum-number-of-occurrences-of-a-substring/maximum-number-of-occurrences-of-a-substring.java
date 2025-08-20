import java.util.*;

class Solution {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        Map<String, Integer> freq = new HashMap<>();
        int res = 0;

        for (int i = 0; i <= s.length() - minSize; i++) {
            String sub = s.substring(i, i + minSize);

            if (countDistinct(sub) <= maxLetters) {
                freq.put(sub, freq.getOrDefault(sub, 0) + 1);
                res = Math.max(res, freq.get(sub));
            }
        }
        return res;
    }

    private int countDistinct(String str) {
        Set<Character> set = new HashSet<>();
        for (char c : str.toCharArray()) {
            set.add(c);
        }
        return set.size();
    }
}
