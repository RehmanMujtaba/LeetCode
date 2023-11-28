class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        element = ""
        for item in nums:
            if count == 0:
                element = item
            
            if item == element:
                count += 1
            else:
                count -= 1
        
        return element