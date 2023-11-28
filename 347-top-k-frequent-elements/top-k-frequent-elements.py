class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for item in nums:
            if item in hashmap:
                hashmap[item] += 1
            else:
                hashmap[item] = 1
        
        counts = [[] for item in range(len(nums) + 1)]
        for key,value in hashmap.items():
            counts[value].append(key)
        
        num = k
        answer = []
        for arr in reversed(counts):
            if num > 0:
                for item in arr:
                    answer.append(item)
                    num -= 1
            else:
                break
        return answer