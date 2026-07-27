class MedianFinder:

    def __init__(self):
        # SMALL CONTAINS SMALL NUMBERS AND PERFORMS TO BE A MAXHEAP 
        # LARGE CONTAINS LARGE NUMBERS AND PERFORMS TO BE A MINHEAP 
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:

        # BY DEFAULT ADDING INTO SMALL 
        heapq.heappush(self.small , -1 * num)

        # ALL THE VALUES IN SMALL MUST SMALL FROM MIN ELEMENT OF LARGE 
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large , -1 * val)
        
        # HANDLING UNEVEN LENGTH

        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large , -1 * val)
            
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small , -1 * val)            


    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1* self.small[0] + self.large[0]) / 2.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()