class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // USING HASHMAP AND BUCKET SORT 

        HashMap<Integer , Integer> FreqCount = new HashMap<>();

        for( int n : nums)
        {
            FreqCount.put(n , FreqCount.getOrDefault(n , 0) + 1);
        }

        List<Integer>[] bucket = new List[nums.length + 1];

        for(int i = 0; i < bucket.length; i++){
            bucket[i] = new ArrayList<>();
        }

        int res[] = new int[k];

        for(Map.Entry<Integer ,Integer> entry: FreqCount.entrySet())
        {
            bucket[entry.getValue()].add(entry.getKey());
        }
        int index = 0;

        for(int i = bucket.length - 1; i >= 0 && index < k; i--){
            for(int num : bucket[i]){
                res[index++] = num;
                if(index == k) break;
            }
        }
        return res;
    }
}



        // USING HASHMAP AND PRIORITY QUEUE 

//         HashMap<Integer , Integer> FrequencyCount = new HashMap<>();

//         for( int i = 0 ; i < nums.length ; i++)
//         {
//             FrequencyCount.put(nums[i] , FrequencyCount.getOrDefault(nums[i],0) + 1);
//         }

//         PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b) -> b[1] - a[1]);
//         for(Map.Entry<Integer,Integer> entry : FrequencyCount.entrySet()){
//             maxHeap.add(new int[]{entry.getKey(), entry.getValue()});
//         }
//         int[] res = new int[k];

//         for(int i = 0; i < k; i++){
//             res[i] = maxHeap.poll()[0];
//         }

//         return res;


        
//     }
// }