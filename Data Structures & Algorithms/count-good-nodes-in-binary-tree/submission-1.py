# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0

        def dfs(root, cur_max):
            if not root:
                return None
            
            self.res += 1 if root.val >= cur_max else 0

            cur_max = max(cur_max, root.val)

            dfs(root.left, cur_max)
            dfs(root.right, cur_max)
        
        dfs(root, root.val)
        return self.res