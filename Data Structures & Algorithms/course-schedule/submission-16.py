class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        indeg = [0] * numCourses

        for i in range(numCourses):
            adj[i] = []

        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
            indeg[prereq] += 1

        q = deque()
        
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        res = 0
        while q:
            crs = q.popleft()
            res += 1

            for nei in adj[crs]:
                indeg[nei] -= 1

                if indeg[nei] == 0:
                    q.append(nei)
        
        return res == numCourses