import java.util.*;

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        List<Integer> res = new ArrayList<>();

        for (int n : nums) {
            hashmap.put(n, hashmap.getOrDefault(n, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
            if (entry.getValue() > nums.length / 3) {
                res.add(entry.getKey());
            }
        }

        return res;
    }
}
