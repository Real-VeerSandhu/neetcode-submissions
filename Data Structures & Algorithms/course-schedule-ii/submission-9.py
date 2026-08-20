class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
            indeg[prereq] += 1


        output = []
        path = set()
        visit = set()

        def dfs(crs):
            if crs in path:
                return False
            # if adj[crs] == []:
            #     return True
            if crs in visit:
                return True
            
            path.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq):
                    return False
            path.remove(crs)
            visit.add(crs)
            # adj[crs] = []
            output.append(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
