class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # print(adj_list)

        self.visit = set()

        def bfs(cur):
            q = deque()
            q.append(cur)

            self.visit.add(cur)

            while q:
                cur = q.popleft()

                for nei in adj_list[cur]:
                    if nei not in self.visit:
                        q.append(nei)
                        self.visit.add(nei)
        res = 0
        for i in range(n):
            if i not in self.visit:
                bfs(i)
                res += 1
        return res
