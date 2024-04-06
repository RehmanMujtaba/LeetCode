from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:

        hashmap = defaultdict(int)  
        sol = []     

        for char in s:
            hashmap[char] += 1
        
        sorted_hashmap = {key: value for key, value in sorted(hashmap.items(), key=lambda item: item[1], reverse=True)}

        for key, value in sorted_hashmap.items():
            sol.append(value * key)
        
        return ''.join(sol)
        