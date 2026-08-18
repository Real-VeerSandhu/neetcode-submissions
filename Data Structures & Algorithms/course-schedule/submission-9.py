class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indeg = [0] * numCourses
        adj = defaultdict(list)

        # crs -> pre1 -> pre2 ->
        # cs246 -> cs 136 -> cs 135

        for crs, pre in prerequisites: 
            indeg[pre] += 1 # pre has += 1 edge going into it
            adj[crs].append(pre)
        
        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0: # no incoming edges -> it can be a source
                q.append(i)
        
        finish = 0

        while q:
            crs = q.popleft()
            finish += 1

            for pre in adj[crs]:
                indeg[pre] -= 1
                if indeg[pre] == 0:
                    q.append(pre)
        
        return finish == numCourses