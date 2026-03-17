class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // USING HASHMAP AND PRIORITY QUEUE 

        HashMap<Integer , Integer> FrequencyCount = new HashMap<>();

        for( int i = 0 ; i < nums.length ; i++)
        {
            FrequencyCount.put(nums[i] , FrequencyCount.getOrDefault(nums[i],0) + 1);
        }

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b) -> b[1] - a[1]);
        for(Map.Entry<Integer,Integer> entry : FrequencyCount.entrySet()){
            maxHeap.add(new int[]{entry.getKey(), entry.getValue()});
        }
        int[] res = new int[k];

        for(int i = 0; i < k; i++){
            res[i] = maxHeap.poll()[0];
        }

        return res;


        
    }
}