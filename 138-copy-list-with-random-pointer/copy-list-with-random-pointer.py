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
        
        arr, new_arr, curr_old, head_new = [], [], head, Node(0)
        curr_new = head_new
        while curr_old is not None:
       #     arr.append(curr_old)
            curr_new.next = Node(curr_old.val)
            curr_new = curr_new.next
            curr_old = curr_old.next
        
        curr_old = head
        curr_new = head_new.next

        while curr_old is not None:
            rand = curr_old.random
            if rand is not None:
                i = 0
                temp = head
                while temp is not rand:
                    temp = temp.next
                    i += 1
                temp = head_new.next
                for index in range(0, i):
                    temp = temp.next
                curr_new.random = temp
            else:
                curr_new.random = None
            curr_old = curr_old.next
            curr_new = curr_new.next
 
        return head_new.next