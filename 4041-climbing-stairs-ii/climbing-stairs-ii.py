class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dijstra (minheap)
        dist = [float("inf")] * (n + 1)
        minheap = [(0 , 0)]
        heapq.heapify(minheap)

        while minheap:
            idx , cst = heapq.heappop(minheap)

            # skip case 
            if cst > dist[idx]:
                continue

            # edge case 
            if idx == n:
                return cst 

            for j in range(idx + 1 , min(n , idx + 3) + 1):
                new_cost = cst + costs[j - 1] + (j - idx) ** 2

                if new_cost < dist[j]:
                    dist[j] = new_cost 
                    heapq.heappush(minheap ,(j , new_cost))

        return dist[n]


        # backtracking + memoization 
        dp = {}
        
        def dfs(i):
            if i == n:
                return 0
            
            if i in dp:
                return dp[i]

            res = float("inf")

            for j in range(i + 1 , min(n , i + 3) + 1):
                res = min(res , costs[j - 1] + (j - i) ** 2 + dfs(j))
            
            dp[i] = res
            return dp[i]

        return dfs(0)


        # brute force

        def dfs(i):
            if i == n:
                return 0
            
            ans = float("inf")

            for j in range(i + 1 , min(n , i + 3) + 1):
                ans = min(ans , costs[j - 1] + (j - i) ** 2 + dfs(j))
            
            return ans 

        return dfs(0)
