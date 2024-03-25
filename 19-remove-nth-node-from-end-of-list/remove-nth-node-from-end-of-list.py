# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        stack = []
        curr = head

        while curr != None:
            stack.append(curr)
            curr = curr.next
        
        popped = 1
        remove = stack.pop()
        
        while popped < n:
            remove = stack.pop()
            popped += 1    
        
        curr = head

        if curr == remove:
            head = curr.next
            return head

        while curr.next != None and curr.next != remove:
            curr = curr.next
    
        curr.next = remove.next
        return head