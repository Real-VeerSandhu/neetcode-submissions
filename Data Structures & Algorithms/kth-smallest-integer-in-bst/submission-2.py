# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []


        def dfs(root):
            visit = [False]
            stack = [root]

            while visit or stack:
                cur = stack.pop()
                seen = visit.pop()

                if not cur:
                    continue
                if seen:
                    res.append(cur.val)
                else:
                    visit.append(False)
                    stack.append(cur.right)
                    visit.append(True)
                    stack.append(cur)
                    visit.append(False)
                    stack.append(cur.left)


        dfs(root)

        return res[k - 1]

