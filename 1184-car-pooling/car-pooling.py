class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key =lambda t:t[1])
        minheap = []
        curpass = 0

        for t in trips:
            pas , st , end = t

            while minheap and minheap[0][0] <= st:
                curpass -= minheap[0][1]
                heapq.heappop(minheap)
            curpass += pas

            if curpass > capacity:
                return False
            heapq.heappush(minheap ,[end , pas])  
        return True

        