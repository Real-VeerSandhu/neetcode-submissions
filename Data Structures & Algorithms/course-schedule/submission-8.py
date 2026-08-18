class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indeg = [0] * numCourses
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            indeg[pre] += 1
            adj[crs].append(pre)
        
        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        finish = 0

        while q:
            node = q.popleft()
            finish += 1

            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses