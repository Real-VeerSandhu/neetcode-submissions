# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_depth(self, root):
        max_depth = 0

        q = deque()

        if root:
            q.append(root)
        else:
            return 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            max_depth += 1
        
        return max_depth - 1
    
    def max_height(self, root):
        if not root:
            return 0
        
        return 1 + max(self.max_height(root.left), self.max_height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        print(self.max_depth(root))
        print(self.max_height(root))

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.res
        

        