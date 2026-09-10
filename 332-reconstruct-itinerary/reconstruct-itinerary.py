class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        stack = ["JFK"]
        res = []
        adj = collections.defaultdict(list)

        for src , des in sorted(tickets)[::-1]:
            adj[src].append(des)


        while stack:
            curr = stack[-1]

            if not adj[curr]:
                res.append(stack.pop())

            else:
                stack.append(adj[curr].pop())
        return res[::-1]


         
        