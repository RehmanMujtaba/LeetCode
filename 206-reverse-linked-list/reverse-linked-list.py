# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_node = head
        last_node = None
        next_node = None
        
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = last_node
            last_node = curr_node
            curr_node = next_node
        curr_node = last_node

        
        return curr_node
