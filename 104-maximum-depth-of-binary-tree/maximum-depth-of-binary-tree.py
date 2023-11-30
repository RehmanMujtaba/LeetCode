# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root != None:
            count_right = self.maxDepth(root.right) if root.right else 0
            count_left = self.maxDepth(root.left) if root.left else 0
            return 1 + max(count_left, count_right)
        else:
            return 0

