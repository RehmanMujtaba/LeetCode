# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isTreeEqual(node1 : Optional[TreeNode], node2 : Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            elif (node1 is None) or (node2 is None):
                return False
            
            if node1.val == node2.val:
                return isTreeEqual(node1.left, node2.right) and isTreeEqual(node1.right, node2.left)
            else:
                return False
            

        return isTreeEqual(root.left, root.right)