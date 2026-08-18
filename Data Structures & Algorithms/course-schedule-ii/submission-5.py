class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        prereq = defaultdict(list)

        for crs, pre in prerequisites:
            indegree[pre] += 1
            prereq[crs].append(pre)

        output = []

        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        while q:
            crs = q.popleft()
            output.append(crs)

            for nei in prereq[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            
        
        return output[::-1] if len(output) == numCourses else []