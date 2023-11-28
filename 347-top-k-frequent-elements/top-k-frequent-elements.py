import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        # Count the frequency of each element
        for item in nums:
            if item in hashmap:
                hashmap[item] += 1
            else:
                hashmap[item] = 1

        # Use a min heap to keep track of the k most frequent elements
        min_heap = []

        for key, value in hashmap.items():
            # Push the first k elements into the heap
            if len(min_heap) < k:
                heapq.heappush(min_heap, (value, key))
            else:
                # If the current element has a higher frequency than the smallest element in the heap, replace it
                if value > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (value, key))

        # Extract the elements from the heap
        result = [element[1] for element in min_heap]

        return result
