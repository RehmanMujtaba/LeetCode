# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tail = None
        head = tail
        curr_1 = l1
        curr_2 = l2
        carry = False

        while curr_1 != None or curr_2 != None:
            digit = 0
            if curr_1:
                digit = curr_1.val
                curr_1 = curr_1.next
            if curr_2:
                digit += curr_2.val
                curr_2 = curr_2.next
            if carry:
                digit += 1
                carry = False            
            if digit >= 10:
                digit = digit % 10
                carry = True
            
            new_Node = ListNode(digit, None)
            prev = tail
            tail = new_Node
            if prev:
                prev.next = tail
            else:
                head = tail
            
        
        if carry:
            new_Node = ListNode(1, None)
            tail.next = new_Node
            tail = new_Node

        return head
