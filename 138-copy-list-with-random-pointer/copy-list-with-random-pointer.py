"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr_old, head_new = head, Node(0)
        curr_new = head_new

        while curr_old is not None:
            curr_new.next = Node(curr_old.val)
            curr_new = curr_new.next
            curr_old = curr_old.next
        
        curr_old = head
        curr_new = head_new.next

        while curr_old is not None:
            rand = curr_old.random
            if rand is not None:
                temp = head
                temp_new = head_new.next
                while temp is not rand:
                    temp = temp.next
                    temp_new = temp_new.next
                curr_new.random = temp_new
            else:
                curr_new.random = None
            curr_old = curr_old.next
            curr_new = curr_new.next
 
        return head_new.next