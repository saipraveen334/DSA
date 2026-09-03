class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set()
        visited = set()

        # creating the dictionary
        preMap = {i : [] for i in range(numCourses)}

        # append the respective prerequisites 
        for crs , pre in prerequisites:
            preMap[crs].append(pre)

        output = []

        def dfs(crs):
            if crs in cycle:
                return False 
            
            if crs in visited:
                return True 
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if  dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True 


        # make sure that every course can be completed 
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output 


        


        