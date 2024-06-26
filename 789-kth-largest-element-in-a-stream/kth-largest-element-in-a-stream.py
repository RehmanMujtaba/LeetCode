import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
            

    def add(self, val: int) -> int:
        if len(self.heap) == 0:
            heapq.heappush(self.heap, val)
            return val
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        if val >= self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)