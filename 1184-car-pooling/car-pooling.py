class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda   t : t[1])
        minHeap  = []  # ( END , NUMPASSENGERS )

        curPass = 0

        for numPass , start , end  in trips:
            while minHeap and minHeap[0][0] <= start:
                end1 , numPass1 = heapq.heappop(minHeap)
                curPass -= numPass1
            
            curPass += numPass 

            if curPass > capacity:
                return False 
            
            heapq.heappush(minHeap ,(end , numPass))

        return True 


        