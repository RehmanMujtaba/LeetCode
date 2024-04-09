# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode() # Dummy Head
        curr = head
        node = None

        l1_curr = l1
        l2_curr = l2

        carry = False

        while l1_curr or l2_curr:
            if l1_curr and l2_curr:
                sum = l1_curr.val + l2_curr.val + carry
                l1_curr = l1_curr.next
                l2_curr = l2_curr.next
            elif l1_curr:
                sum = l1_curr.val + carry
                l1_curr = l1_curr.next 
            else:
                sum = l2_curr.val + carry
                l2_curr = l2_curr.next
                        
            if sum >= 10:
                node = ListNode(sum % 10)
                carry = True
            else:
                node = ListNode(sum)
                carry = False
            
            curr.next = node
            curr = curr.next
        
        if carry:
            curr.next = ListNode(1)
        
        return head.next


