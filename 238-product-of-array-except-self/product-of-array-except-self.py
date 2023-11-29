class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        return_arr = [1] * len(nums)

        product = 1

        for i in range(len(nums)):
            return_arr[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            return_arr[i] *= product
            product *= nums[i]
        
        return return_arr
    
    




