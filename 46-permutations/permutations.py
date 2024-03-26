from typing import List
class Solution:  
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(remaining_nums, permutation):
            if not remaining_nums:
                ans.append(permutation)
                return

            for i in range(len(remaining_nums)):
                backtrack(remaining_nums[:i] + remaining_nums[i+1:], permutation + [remaining_nums[i]])

        ans = []
        backtrack(nums, [])
        return ans