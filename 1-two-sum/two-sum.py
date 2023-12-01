class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i, num1 in enumerate(nums):
        #     for j, num2 in enumerate(nums[i+1:], start = i+1):
        #         if i != j and num1 + num2 == target:
        #             return [i,j]


        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = i

        for i,num in enumerate(nums):
            if target - num in hashmap and hashmap[target - num] != i:
                return [i, hashmap[target-num]]