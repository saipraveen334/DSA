class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] people) {

        int n = people.length;
        int[] res = new int[n];

        int[][] persons = new int[n][2];
        for (int i = 0 ; i < n ; i++)
        {
            persons[i][0] = people[i];
            persons[i][1] = i ;
        }
        Arrays.sort(persons , (a,b) -> Integer.compare(a[0] , b[0])) ;
        Arrays.sort(flowers , (a,b) -> Integer.compare(a[0] , b[0])) ;

        PriorityQueue<Integer> heap = new PriorityQueue<>();

        int j = 0 ;

        for(int[] person : persons)
        {
            int p = person[0] ;
            int idx = person[1] ;

            while( j < flowers.length && flowers[j][0] <= p)
            {
                heap.offer(flowers[j][1]) ;
                j ++ ;
            }
            while( !heap.isEmpty() && heap.peek() < p)
            {
                heap.poll() ;
            }
            res[idx] = heap.size();
        }

        return res;

        

    }
}