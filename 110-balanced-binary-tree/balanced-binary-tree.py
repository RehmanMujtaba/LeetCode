# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root != None:
            depth_left = self.maxDepth(root.left)
            depth_right = self.maxDepth(root.right)
            print(f"height of left subtree is {depth_left} and right is {depth_right}")
            if abs(depth_left - depth_right) <= 1:
                return True and self.isBalanced(root.right) and self.isBalanced(root.left)
            else:
                return False
        else:
            return True
            
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root != None:
            depth_left = self.maxDepth(root.left)
            depth_right = self.maxDepth(root.right)
            return 1 + max(depth_left, depth_right)
        else:
            return 0