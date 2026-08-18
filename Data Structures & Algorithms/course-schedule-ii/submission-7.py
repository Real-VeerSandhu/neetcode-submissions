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
        
        output = []

        while q:
            crs = q.popleft()
            output.append(crs)

            for pre in adj[crs]:
                indeg[pre] -= 1
                if indeg[pre] == 0:
                    q.append(pre)
        
        return output[::-1] if len(output) == numCourses else []