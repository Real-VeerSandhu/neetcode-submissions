class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # make adj_list

        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        
        seen = set()
        
        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)

            for nei in adj_list[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
                
            return True
        
        return dfs(0, -1) and len(edges) == (n-1)
