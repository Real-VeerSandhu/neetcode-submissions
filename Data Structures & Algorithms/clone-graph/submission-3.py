"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def bfs(node):
            q = deque()
            q.append(node)
            oldToNew[node] = Node(node.val)

            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    for nei in cur.neighbors:
                        if nei in oldToNew:
                            oldToNew[cur].neighbors.append(oldToNew[nei])
                            continue
                        oldToNew[nei] = Node(nei.val)
                        q.append(nei)
                        oldToNew[cur].neighbors.append(oldToNew[nei])

            return oldToNew[node]
        
        return bfs(node) if node else None