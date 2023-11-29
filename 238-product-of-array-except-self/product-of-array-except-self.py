class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_arr = []
        postfix_arr = []

        product = 1

        for index, num in enumerate(nums):
            product = product * num
            prefix_arr.append(product)
        
        product = 1

        for index, num in enumerate(reversed(nums)):
            product = product * num
            postfix_arr.append(product)
        
        postfix_arr = postfix_arr[::-1]

        return_arr = [1] * len(nums)

        for index in range(len(nums)):
            if index == 0:
                return_arr[index] = 1 * postfix_arr[index + 1]
            elif index == len(nums) - 1:
                return_arr[index] = 1 * prefix_arr[index - 1]
            else:
                return_arr[index] = prefix_arr[index - 1] * postfix_arr[index + 1]
            
        return return_arr

