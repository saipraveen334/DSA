class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        kMost = [0] * k
        available = SortedList(range(k))
        unavail = []

        for i in range(len(arrival)):
            arr = arrival[i]

            while unavail and unavail[0][0] <= arr:
                t, server = heapq.heappop(unavail)
                available.add(server)

            if not available:
                continue

            mid = i % k
            pos = available.bisect_left(mid)

            if pos == len(available):
                pos = 0

            used = available.pop(pos)
            kMost[used] += 1

            heapq.heappush(unavail, (arr + load[i], used))

        maximum = max(kMost)
        return [i for i in range(k) if kMost[i] == maximum]

        
        kMost = [0] * k 
        server = [[i , 1] for i in range(k)]
        unavail = []
        
        for i in range(len(arrival)):
            arr = arrival[i]
            reqtime = load[i]
            tt = arr + reqtime

            while unavail and unavail[0][0] <= arr:
                t , kth = heapq.heappop(unavail)
                server[kth][1] = 1
            
            flag = True 

            mid = (i % k)

            for j in range(mid , k):
                if server[j][1] == 1:
                    heapq.heappush(unavail , (tt , j))
                    server[j][1] = -1
                    used = j
                    flag = False
                    break
            if flag:
                for l in range(0 , mid):
                    if server[l][1] == 1:
                        heapq.heappush(unavail ,(tt , l))
                        server[l][1] = -1
                        used = l
                        flag = False 
                        break
            if flag:
                continue
            else:
                kMost[used] += 1
        
        maxUsed = max(kMost)
        res = []

        for i in range(len(kMost)):
            if kMost[i] == maxUsed:
                res.append(i)
        
        return res


        
            


            



        