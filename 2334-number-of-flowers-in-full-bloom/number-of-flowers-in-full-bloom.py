class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people =[(p,i) for i,p in enumerate(people)]
        res = [0] * len(people)

        start = [f[0] for f in flowers]
        end = [f[1] for f in flowers]
        heapq.heapify(start)
        heapq.heapify(end)
        count = 0  

        for p , i in sorted(people):

            while start and start[0] <= p:
                heapq.heappop(start)
                count += 1
            while end and end[0] < p:
                heapq.heappop(end)
                count -= 1
            res[i] = count

        return res

        