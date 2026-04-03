class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        heap =[]

        for r in range(len(nums)):
            heapq.heappush(heap , (-nums[r] , r))

            if r >= k - 1:

                while heap[0][1] <= r - k:
                    heapq.heappop(heap)

                ans.append(-heap[0][0])
        return ans






        # res = []

        # q = deque() #INDEX 
        # l = r = 0

        # while r < len(nums):

        #     while q and nums[r] > nums[q[-1]]:
        #         q.pop()

        #     q.append(r)

        #     if l > q[0]:
        #         q.popleft()
            
        #     if (r + 1) >= k:
        #         res.append(nums[q[0]])
        #         l += 1
        #     r += 1
        # return res
        

            

