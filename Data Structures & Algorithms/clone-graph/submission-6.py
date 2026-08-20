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
        

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque()

        q.append(node)

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for nei in cur.neighbors:
                    if nei not in old_to_new:
                        old_to_new[nei] = Node(nei.val)
                        q.append(nei)
                    old_to_new[cur].neighbors.append(old_to_new[nei])
        
        if not node:
            return None
        return old_to_new[node]