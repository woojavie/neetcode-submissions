# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        diff = self.height(root.left) - self.height(root.right)
        if diff > 1 or diff < -1:
            return False
        return self.isBalanced(root.left) & self.isBalanced(root.right)
        
    def height(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))