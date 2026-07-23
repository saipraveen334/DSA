class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        maxheap = [-x for x in counter.values()]

        heapq.heapify(maxheap)
        time = 0
        q = deque()
        
        while q or maxheap:

            time += 1

            if maxheap:

                #DECREASE THE COUNT 
                cnt = 1 + heapq.heappop(maxheap)

                if cnt:
                    q.append([cnt , time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(maxheap , q.popleft()[0])
        return time




        