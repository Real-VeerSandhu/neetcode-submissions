class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        for n in range(numCourses):
            prereq[n] = []
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        path = set()
        visit = set()
        output = []

        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            
            path.add(crs)
            for nei in prereq[crs]:
                if not dfs(nei):
                    return False
            path.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return output