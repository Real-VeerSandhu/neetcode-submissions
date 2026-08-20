# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        

        stack = [(root, False)]
        res = []

        while stack:
            cur, seen = stack.pop()
            if not cur:
                res.append((True, 0))
                continue
            if seen:
                left_valid, left_h = res.pop()
                right_valid, right_h = res.pop()

                cur_h = 1 + max(left_h, right_h)
                cur_valid = left_valid and right_valid and abs(left_h - right_h) <= 1

                if not cur_valid:
                    return False

                res.append((cur_valid, cur_h))

            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
        

        return True
        
