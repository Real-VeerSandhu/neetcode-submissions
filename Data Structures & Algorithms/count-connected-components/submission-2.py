class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for v1,v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        visit = [False] * n

        def dfs(node):
            for nei in adj_list[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        c = 0
        for node in adj_list:
            if not visit[node]:
                visit[node] = True
                dfs(node)
                c+=1

        return c


