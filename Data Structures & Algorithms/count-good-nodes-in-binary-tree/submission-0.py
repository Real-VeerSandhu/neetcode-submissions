# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        
        def dfs(cur, rolling_max):
            if not cur:
                return
            if rolling_max <= cur.val:
                self.good_nodes += 1
            
            rolling_max = max(rolling_max, cur.val)
            dfs(cur.left, rolling_max)
            dfs(cur.right, rolling_max)

        dfs(root, root.val)
        return self.good_nodes