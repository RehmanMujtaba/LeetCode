# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    node_list = []

    def __init__(self, head: Optional[ListNode]):
        self.node_list = []
        curr = head
        while(curr):
            self.node_list.append(curr.val)
            curr = curr.next
        print(self.node_list)


    def getRandom(self) -> int:
        num = randint(0,len(self.node_list)-1)

        return self.node_list[num]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()