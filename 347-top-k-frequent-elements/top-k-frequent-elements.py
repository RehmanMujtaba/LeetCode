import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use Counter to count frequencies
        freq_counter = Counter(nums)

        # Use a min heap to keep track of the k most frequent elements
        min_heap = [(-freq, num) for num, freq in freq_counter.items()]
        heapq.heapify(min_heap)

        # Extract the k most frequent elements from the min heap
        result = [heapq.heappop(min_heap)[1] for _ in range(k)]

        return result
