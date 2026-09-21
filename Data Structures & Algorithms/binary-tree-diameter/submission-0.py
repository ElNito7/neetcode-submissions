# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0

        def dfs(root: Optional[TreeNode]):
            nonlocal d

            if not root:
                return 0 

            lh = dfs(root.left)
            rh = dfs(root.right)
            d = max(d, lh + rh)

            return 1 + max(rh, lh)
        
        dfs(root)
        return d