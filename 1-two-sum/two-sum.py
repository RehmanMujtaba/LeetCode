class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        sol = []

        for i, num in enumerate(nums):
            if (target - num) in hashmap:
                sol.append(i)
                sol.append(hashmap[target - num])
                return sol
            else:
                hashmap[num] = i
        
