class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}

        for index, num in enumerate(nums):
            hm[num] = index
        
        for index, num in enumerate(nums):
            if target - num in hm:
                if hm[target - num] == index:
                    continue
                return[index, hm[target-num]]