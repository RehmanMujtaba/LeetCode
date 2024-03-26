class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]] 
        else:
            result = []
            for i in range(len(nums)):
                current_num = nums[i]
                remaining_nums = nums[:i] + nums[i+1:]  
                for perm in self.permute(remaining_nums):   
                    result.append([current_num] + perm) 
            return result
