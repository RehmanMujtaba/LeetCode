# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        arr = []
        
        curr = head
        while curr != None:
            arr.append(curr)
            curr = curr.next
        
        num = len(arr) - n
        ToRemove = arr[num]

        if ToRemove == head:
            head = head.next
            return head
        
        prev = arr[num - 1]
        
        prev.next = ToRemove.next
        return head
        