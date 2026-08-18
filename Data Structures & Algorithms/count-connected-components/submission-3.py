class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)

            for nei in adj_list[node]:
                dfs(nei)
        
        comps = 0

        for i in range(n):
            if i in visit:
                # print('conintued @', i)
                continue
            else:
                comps += 1
                # print('comps is now', comps)
                dfs(i)

        return comps
        
        
        
