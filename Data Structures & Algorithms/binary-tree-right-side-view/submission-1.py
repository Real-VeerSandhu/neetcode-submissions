# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        def bfs(cur):
            q = deque()

            if cur:
                q.append(cur)
            
            while q:
                lvl = []
                for i in range(len(q)):
                    cur = q.popleft()

                    lvl.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                self.res.append(lvl[-1])
        
        bfs(root)

        return self.res