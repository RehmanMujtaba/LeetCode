class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums_again = [-num for num in nums]
        heapq.heapify(nums_again)

        x = nums_again[0]
        for i in range(0,k):
            x = heapq.heappop(nums_again)
        
        return -x