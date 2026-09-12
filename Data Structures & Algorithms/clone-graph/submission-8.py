"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        adj_list = {}
        
        old_to_new = {}

        def bfs(cur):
            q = deque()
            q.append(cur)


            old_to_new[cur] = Node(cur.val)

            while q:
                cur = q.popleft()
                print('->', cur.val)

                for nei in cur.neighbors:
                    if nei not in old_to_new:
                        q.append(nei)
                        old_to_new[nei] = Node(nei.val)
                    old_to_new[cur].neighbors.append(old_to_new[nei])
            
           
        
        bfs(node)
        return old_to_new[node]