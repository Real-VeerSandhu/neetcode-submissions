# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # account for negative numbers
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            self.res = max(self.res, root.val + left_max + right_max) # make root the middle/split
            return root.val + max(left_max, right_max) # no split, single lie
        
        dfs(root)
        return self.res