import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        currMax = -inf

        for num in nums: 
     
            if len(heap) < k:
                heappush(heap, num)
            elif heap[0] < num:
                heappop(heap)
                heappush(heap, num)
                if num > currMax:
                    currMax == num   
                    if num > heap[-1]:
                        print("smth")
                        return

        return heap[0]
