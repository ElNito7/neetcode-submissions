# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverse(self, current_node: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = current_node.right
        current_node.right = current_node.left
        current_node.left = temp
        if current_node.left and (current_node.left.left or current_node.left.right):
            self.reverse(current_node.left)
        if current_node.right and (current_node.right.left or current_node.right.right):
            self.reverse(current_node.right)
        return current_node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            return self.reverse(root)
        return root