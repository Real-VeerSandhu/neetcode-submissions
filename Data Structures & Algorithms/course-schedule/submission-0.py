class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to its prereq

        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set() # store all courses along current DFS path

        def dfs(crs):
            if crs in visiting:
                return False # CYCLE
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            preMap[crs] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
