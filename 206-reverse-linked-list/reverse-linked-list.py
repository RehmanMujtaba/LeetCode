# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
with open("user.out", "w") as Solution:
    for tcase in stdin:
        tcase = loads(tcase)
        Solution.write(str(list(reversed(tcase))).replace(" ", "") +"\n")
exit(0)
        
