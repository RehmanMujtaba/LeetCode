from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:

        hashmap = defaultdict(int)  
        sol = []   
        heap = []  

        for char in s:
            hashmap[char] += 1
        
        for key, value in hashmap.items():
            heappush(heap, [-value, key])

        while len(heap) != 0:
            count, letter = heappop(heap)
            sol.append(letter * (-count))
        
        return ''.join(sol)
        