# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0

        def bfs(cur):
            q = deque()

            if cur:
                q.append(cur)
            
            while q:
                self.depth += 1
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
        
        bfs(root)
        return self.depth