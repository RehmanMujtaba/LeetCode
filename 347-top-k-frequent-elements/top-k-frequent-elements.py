import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = defaultdict(int)
        heap = []

        for num in nums:
            hashmap[num] += 1
        
        for key, value in hashmap.items():
            if (len(heap) < k):
                heappush(heap, [value, key])
            elif (heap[0][0] < value):
                heappop(heap)
                heappush(heap, [value, key])

        return  [key for _, key in heap]