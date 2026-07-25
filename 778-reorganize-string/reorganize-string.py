class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        maxheap = [[-cnt , char] for char , cnt in counter.items()]


        heapq.heapify(maxheap)
        res = ""
        prev = None

        while maxheap or prev:

            if prev and not maxheap:
                return ""

            cnt , ch = heapq.heappop(maxheap)
            cnt += 1
            res += ch 

            if prev:
                heapq.heappush(maxheap , prev)
                prev = None 
                
            if cnt != 0:
                prev = [cnt , ch]

        return res



        