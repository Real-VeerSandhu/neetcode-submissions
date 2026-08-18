# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 2 facts
        # 1st fact: first value in preorder traversal = ROOT of the sub tree ur on
        # 2nd fact: every value to the left of the root, will be in left subtree
        # every value to the right of root will be in right subtree

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1 :])

        return root