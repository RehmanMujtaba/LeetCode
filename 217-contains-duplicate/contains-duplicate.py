class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        theMap = {}

        for num in nums:
            if num not in theMap:
                theMap[num] = 1
            else:
                theMap[num] += 1

        for count in theMap.values():
            if count > 1 :
                return True
        return False