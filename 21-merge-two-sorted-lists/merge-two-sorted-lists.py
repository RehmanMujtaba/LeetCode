# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None

        if list1 and list2:
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        else:
            if list1:
                head = list1
                list1 = list1.next
            elif list2:
                head = list2
                list2 = list2.next
            else:
                return head
        
        curr = head
        print(head.val)

        while(list1 or list2) :
            new_node = None
            if (list2 and not list1):
                new_node = list2
                list2 = list2.next
                print(curr.val)
            elif (list1 and not list2) or list1.val < list2.val:
                new_node = list1
                list1 = list1.next
                print(curr.val)
            else:
                new_node = list2
                list2 = list2.next
                print(curr.val)
            curr.next = new_node
            curr = new_node
        return head
            