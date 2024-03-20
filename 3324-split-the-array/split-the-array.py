class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > 2:
                return False
        
        return True