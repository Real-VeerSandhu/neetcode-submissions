class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            indeg[pre] += 1
            adj[crs].append(pre)

        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        visit = set()
        path = set()
        output = []

        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            
            path.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output


