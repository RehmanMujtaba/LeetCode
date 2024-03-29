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
        Q_Queue = deque()

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
        Q_Queue.append(curr)
        while True:
            if q.val == curr.val:
                print(curr.val)
                Q_Queue.append(curr)
                break
            elif q.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            Q_Queue.append(curr)

        ans = None
        while P_Queue[0] == Q_Queue[0]:
            ans = P_Queue.popleft()
            Q_Queue.popleft()

        return ans
