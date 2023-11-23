class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        theMap = {}

        for num in nums:
            if num in theMap:
                return True
            else:
                theMap[num] = 1
        return False