class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for item in nums:
            hashmap[item] = 1 + hashmap.get(item,0)
        
        counts = [[] for item in range(len(nums) + 1)]
        for key,value in hashmap.items():
            counts[value].append(key)
        
        answer = []
        for arr in reversed(counts):
            if k > 0:
                for item in arr:
                    answer.append(item)
                    k -= 1
            else:
                return answer
        return answer