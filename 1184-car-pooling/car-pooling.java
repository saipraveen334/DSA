import java.util.*;

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        Arrays.sort(trips, (a, b) -> Integer.compare(a[1], b[1]));
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int curPass = 0;

        for (int[] t : trips) {
            int pas = t[0], st = t[1], end = t[2];

            while (!minHeap.isEmpty() && minHeap.peek()[0] <= st) {
                curPass -= minHeap.poll()[1];
            }
            curPass += pas;

            if (curPass > capacity) {
                return false;
            }
            minHeap.offer(new int[]{end, pas});
        }
        return true;
    }
}
