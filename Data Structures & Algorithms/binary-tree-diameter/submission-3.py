# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        height = leftHeight + rightHeight
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiamater = self.diameterOfBinaryTree(root.right)
        return max(height, leftDiameter, rightDiamater)
    
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return 1 + max(leftHeight, rightHeight)