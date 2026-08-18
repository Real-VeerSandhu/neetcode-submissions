# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        right = float('inf')
        left = float('-inf')
        cur = root

        def valid(cur, left, right):
            if not cur:
                return True
            if not (left < cur.val < right):
                return False
            
            return valid(cur.left, left, cur.val) and valid(cur.right, cur.val, right)
        
        return valid(root, left, right)