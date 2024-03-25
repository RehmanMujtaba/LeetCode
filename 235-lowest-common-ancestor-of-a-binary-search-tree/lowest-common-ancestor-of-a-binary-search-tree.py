from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        P_Queue = deque()

        curr = root
        P_Queue.append(curr)
        while True:
            if p.val == curr.val:
                P_Queue.append(curr)
                break
            elif p.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            P_Queue.append(curr)
         
        curr = root
        curr_path = P_Queue.popleft()
        ans = root

        while curr == curr_path:
            ans = curr
            if q.val < curr.val:
                curr = curr.left
            elif q.val > curr.val:
                curr = curr.right
            curr_path = P_Queue.popleft()

        return ans
            
        
        
        