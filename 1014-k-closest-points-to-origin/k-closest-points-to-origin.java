class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> minheap = new  PriorityQueue<>(Comparator.comparing( a -> a[0]));

        for(int[] p: points)
        {
            int dist = p[0] * p[0] + p[1] * p[1];

            minheap.offer(new int[] {dist , p[0] , p[1]});
        }

        int[][] res = new int[k][2];

        for(int i = 0 ; i < k ; i++)
        {
            int[] point = minheap.poll();
            res[i] = new int[]{point[1] , point[2]};
        }

        return res;


        
    }
}