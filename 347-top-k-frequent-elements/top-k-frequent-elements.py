import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        heap = []

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        for key, value in hashmap.items():
            if (len(heap) < k):
                heappush(heap, [value, key])
            elif (heap[0][0] < value):
                heappop(heap)
                heappush(heap, [value, key])

        sol = []

        for pair in heap:
            sol.append(pair[1])
        
        return sol