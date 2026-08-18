class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for nei in adj_list[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            
            return True
       
        return dfs(0, -1) and len(visit) == n
