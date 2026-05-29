# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.biggerCount(root, root.val)
    

    def biggerCount(self, root, maxSoFar):
        num = 0
        if not root:
            return 0
        if root.val >= maxSoFar:
            maxSoFar = root.val
            num += 1
        return num + self.biggerCount(root.left, maxSoFar) + self.biggerCount(root.right, maxSoFar)