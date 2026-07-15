class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [-x for x in nums]
        heapq.heapify(minheap)

        while k > 0 and minheap:

            val = heapq.heappop(minheap)
            k -= 1
        
        return -val



        