class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
            indeg[prereq] += 1

        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)


        output = []
        
        while q:
            for _ in range(len(q)):
                crs = q.popleft()

                output.append(crs)

                for prereq in adj[crs]:
                    indeg[prereq] -= 1
                    if indeg[prereq] == 0:
                        q.append(prereq)
        
        return output[::-1] if len(output) == numCourses else []