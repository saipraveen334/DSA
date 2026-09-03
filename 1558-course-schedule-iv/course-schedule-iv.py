class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adjList = {i: [] for i in range(numCourses)}

        for i, j in prerequisites:
            adjList[i].append(j)

        memo = {}

        def dfs(node, target):

            if (node, target) in memo:
                return memo[(node, target)]

            if node == target:
                return True

            for crs in adjList[node]:
                if dfs(crs, target):
                    memo[(node, target)] = True
                    return True

            memo[(node, target)] = False
            return False

        res = []

        for i, j in queries:
            res.append(dfs(i, j))

        return res