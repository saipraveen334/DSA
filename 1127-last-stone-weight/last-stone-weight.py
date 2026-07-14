class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        minheap = [-x for x in stones]
        heapq.heapify(minheap)


        while len(minheap) > 1:
            stone1 = heapq.heappop(minheap)
            stone2 = heapq.heappop(minheap)

            if stone1 == stone2:
                continue
            
            else:
                val = abs(stone1 - stone2)
                heapq.heappush(minheap , - val)
        
        return abs(minheap[0]) if minheap else 0
        


        