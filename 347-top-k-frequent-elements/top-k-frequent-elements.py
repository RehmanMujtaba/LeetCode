
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
        max_heap = [(-value, key) for key, value in hashmap.items()]
        heapq.heapify(max_heap)

        # Extract the k most frequent elements from the max heap
        result = [heapq.heappop(max_heap)[1] for idk in range(k)]

        return result