class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if hashmap.get(num) == 2:
                return False
            hashmap[num] = hashmap.get(num, 0) + 1
            
        
        return True