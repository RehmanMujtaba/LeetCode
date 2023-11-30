# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.maxDepth(root)[0]
            
#   Returns the if the tree is balanced and its max depth
    def maxDepth(self, root: Optional[TreeNode]) -> [bool, int]:
        if root != None:
            depth_left = self.maxDepth(root.left)
            depth_right = self.maxDepth(root.right)
            isBalanced = depth_left[0] and depth_right[0] and abs(depth_right[1] - depth_left[1]) <= 1
            return [isBalanced, 1 + max(depth_left[1], depth_right[1])]
        else:
            return [True, 0]