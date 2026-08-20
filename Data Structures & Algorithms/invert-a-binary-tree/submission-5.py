# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:



        stack = [(root, False)]
        while stack:
            cur, seen = stack.pop()
            if not cur:
                continue
            if seen:
                # do reversal!!
                cur.left, cur.right = cur.right, cur.left
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
        
        return root