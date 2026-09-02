class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # you can take one or more courses by completing 1 course
        # if cycle is detected then return false 
        preMap = {i : [] for i in range(numCourses)}

        for course , pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False 
        return True         