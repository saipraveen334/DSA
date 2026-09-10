class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append([v, w])

        def bfs(k, time):

            q = [(time, k)]   # min heap
            visit = set()

            while q:

                t, src = heapq.heappop(q)

                if src in visit:
                    continue

                visit.add(src)

                if len(visit) == n:
                    return t

                for tar, t1 in adj[src]:

                    if tar in visit:
                        continue

                    heapq.heappush(q, (t + t1, tar))

            return -1

        return bfs(k, 0)