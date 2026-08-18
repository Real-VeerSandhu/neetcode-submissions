# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, cur):
        if not cur:
            return 0

        return 1 + max(self.depth(cur.left), self.depth(cur.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)