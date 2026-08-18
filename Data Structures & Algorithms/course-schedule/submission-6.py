class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        path = set()

        def dfs(crs):
            if crs in path:
                return False
            if adj[crs] == []:
                return True
            
            path.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            path.remove(crs)
            adj[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True