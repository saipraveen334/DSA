class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = collections.defaultdict(list)

        for u, v, price in flights:
            adj[u].append([v, price])

        q = collections.deque()
        q.append([src, 0])

        cost = [float("inf")] * n
        cost[src] = 0

        k += 1

        while q and k > 0:

            size = len(q)
            temp = cost.copy()

            for _ in range(size):

                cur, curCost = q.popleft()

                for nei, price in adj[cur]:

                    if curCost + price < temp[nei]:
                        temp[nei] = curCost + price
                        q.append([nei, curCost + price])

            cost = temp
            k -= 1

        return cost[dst] if cost[dst] != float("inf") else -1