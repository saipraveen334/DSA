class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # sorting + sliding window + hashmap 
        logs.sort(key = lambda x : x[1])
        sq = sorted((q , i) for i , q in enumerate(queries))
        res = [0] * len(queries)

        left = 0
        right = 0 
        active = 0 
        freq = {}

        for q , idx in sq:
            # adding the active queries till q (inclusive)
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                freq[server] = freq.get(server , 0) + 1

                # add active query for every new log id 
                if freq[server] == 1:
                    active += 1

                right += 1
            # remove the active queries till q - x (inclusive)
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                freq[server] -= 1

                # remove / delete the active query 
                if freq[server] == 0:
                    active -= 1
                    del freq[server]
                left += 1

            res[idx] = n - active 

        return res 

        # brute force 
        logs.sort(key=lambda x: x[1])
        res = []
        base = set(range(1, n + 1))

        def getCount(qRange):
            reach = set()
            for k in logs:
                if qRange - x <= k[1] <= qRange:
                    reach.add(k[0])
            return reach

        for q in queries:
            ans = getCount(q)
            res.append(len(base - ans))

        return res