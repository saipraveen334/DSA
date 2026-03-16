class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqcount = {} # NUMBER - > FREQUENCY COUNT

        res = []

        for n in nums:
            freqcount[n] = 1 + freqcount.get(n,0)

        maxheap = []

        for num , count in freqcount.items():
            heapq.heappush(maxheap, (-count , num))
        
        while maxheap and k > 0:
            val , n = heapq.heappop(maxheap)
            res.append(n)
            k-= 1

        return res

        

        



        # res = []
        # FrequencyMap = {} # number -> frequency count

        # for n in nums:
        #     FrequencyMap[n] = 1 + FrequencyMap.get(n,0)
        
        # bucket =[[] for _ in range(len(nums)+1)]

        # for n,fcount in FrequencyMap.items():
        #     bucket[fcount].append(n) 
        
        # for i in range(len(nums) , 0 , -1):
        #     for num in bucket[i]:
        #         res.append(num)

        #         if k == len(res):
        #             return res
            




        
        
        