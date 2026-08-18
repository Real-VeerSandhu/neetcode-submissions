class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}

        for c in range(numCourses):
            prereq[c] = []
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        output = []
        visit = set()
        path = set()

        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            
            path.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output