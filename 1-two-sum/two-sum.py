class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}

        for index, num in enumerate(nums):
            if target - num in hm:
                return [hm[target - num], index]
            else:
                hm[num] = index