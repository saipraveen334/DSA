import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];

            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            // Convert count array into a unique key string
            String key = Arrays.toString(count);

            res.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(res.values());
    }
}
