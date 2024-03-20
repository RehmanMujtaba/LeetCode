class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                if hashmap[num] == 2:
                    return False
                else:
                    hashmap[num] = 2
            else:
                hashmap[num] = 1
        
        return True