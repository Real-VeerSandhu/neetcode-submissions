# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(cur, left, right):
            if not cur:
                return True
            if not (cur.val > left and cur.val < right):
                return False
            return dfs(cur.left, left, cur.val) and dfs(cur.right, cur.val, right)
        
        return dfs(root, -1001, 1001)