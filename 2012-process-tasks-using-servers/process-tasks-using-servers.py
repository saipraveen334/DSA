class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        res = [0] * len(tasks)
        availble = [(s , i) for i , s in enumerate(servers)]
        heapq.heapify(availble)
        unavail = []
        t = 0

        for i in range(len(tasks)):
            t = max(t , i)

            if len(availble) == 0:
                t = unavail[0][0]
            
            while unavail and unavail[0][0] <= t:
                ptime , w , idx = heapq.heappop(unavail)
                heapq.heappush(availble , (w , idx))
            
            w , idx = heapq.heappop(availble)
            res[i] = idx
            heapq.heappush(unavail , (tasks[i] + t , w , idx))
        return res
        






