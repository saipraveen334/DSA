import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {

        List<Integer> res = new ArrayList<>();
        Deque<Integer> q = new ArrayDeque<>(); // stores indices

        int l = 0;

        for (int r = 0; r < nums.length; r++) {

            // remove smaller elements from back
            while (!q.isEmpty() && nums[r] > nums[q.peekLast()]) {
                q.pollLast();
            }

            q.offerLast(r);

            // remove left element if out of window
            if (l > q.peekFirst()) {
                q.pollFirst();
            }

            // window formed
            if (r + 1 >= k) {
                res.add(nums[q.peekFirst()]);
                l++;
            }
        }

        // convert List to array
        int[] ans = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            ans[i] = res.get(i);
        }

        return ans;
    }
}