class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # m = len(edges)
        
        # if n != m - 1:
        #     return False
        
        # assert(n == m - 1)

        adj = {}
        for i in range(n):
            adj[i] = []
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n