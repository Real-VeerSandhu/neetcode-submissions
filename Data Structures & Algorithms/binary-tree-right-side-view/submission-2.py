# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()

        if root:
            q.append(root)

        while q:
            rightSide = None
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    rightSide = cur
                    q.append(cur.left)
                    q.append(cur.right)
            if rightSide:
                res.append(rightSide.val)
        return res