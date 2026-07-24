class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i , t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda x : x[0])

        minheap = []
        res = []
        i = 0
        time = tasks[0][0]

        while minheap or i < len(tasks):

            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minheap , [tasks[i][1] , tasks[i][2]])
                i += 1
            if not minheap:
                time = tasks[i][0]
            else:
                processtime , ind = heapq.heappop(minheap)
                time += processtime 
                res.append(ind)
        return res


            







        